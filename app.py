import psycopg2
from config import config
from flask import Flask, render_template, request

# Connect to the PostgreSQL database server
def connect(query):
    conn = None
    rows = ''
    try:
        # read connection parameters
        params = config()
 
        # connect to the PostgreSQL server
        print('Connecting to the %s database...' % (params['database']))
        conn = psycopg2.connect(**params)
        print('Connected.')
      
        # create a cursor
        cur = conn.cursor()
        
        # execute a query using fetchall()
        cur.execute(query)
        rows = cur.fetchall()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
    # return the query result from fetchall()
    return rows

 
# app.py
app = Flask(__name__)


# serve form web page
@app.route("/")
def form():
    return render_template('my-form.html')

# handle solar programs POST and serve result web page
@app.route('/solar_programs_handler', methods=['POST'])
def solar_programs_handler(): 
    rows = connect('CREATE VIEW mun_elec AS SELECT municipality_index, year, residential_electricity, commercial_electricity, industrial_electricity, street_light_electricity FROM municipality WHERE municipality.municipality_index = ' + request.form['municipality_index'] + '; UPDATE mun_elec SET residential_electricity=0 WHERE residential_electricity IS NULL; UPDATE mun_elec SET commercial_electricity=0 WHERE commercial_electricity IS NULL; UPDATE mun_elec SET industrial_electricity=0 WHERE industrial_electricity IS NULL; UPDATE mun_elec SET street_light_electricity=0 WHERE street_light_electricity IS NULL; SELECT m.year, mc.municipality_name, mc.county, count(s.application_number), (m.residential_electricity + m.commercial_electricity + m.industrial_electricity + m.street_light_electricity) FROM solar_installation_programs s, municipality_code mc, mun_elec m WHERE EXTRACT(year FROM s.pto_date) < m.year+1 AND s.municipality_index = ' + request.form['municipality_index'] + ' AND mc.municipality_index = ' + request.form['municipality_index'] + ' AND m.municipality_index = ' + request.form['municipality_index'] + ' GROUP BY m.year, mc.municipality_name, mc.county, m.residential_electricity, m.commercial_electricity, m.street_light_electricity, m.industrial_electricity ORDER BY m.year;')
    heads = ['Year', 'Municipality', 'County', 'Number of Solar Installations', 'Total Electricity Usage (kWh)']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle energy efficiency program POST and serve result web page
@app.route ('/ee_handler', methods=['POST'])
def ee_handler():
    rows = connect('SELECT mc.municipality_index, mc.municipality_name, mc.county, e.total_completed_projects, g.total_co2, c.population FROM municipality_code mc, energy_efficiency_programs e, ghg_emissions g, community_profile c WHERE e.municipality_index = mc.municipality_index AND g.municipality_index = mc.municipality_index AND c.municipality_index = mc.municipality_index AND c.year = 2020 AND g.year =2020 AND c.population > ' + request.form["pop_min"] + ' AND c.population < '+ request.form['pop_max'] + ' ORDER BY c.population;')
    heads = ['Municipality Index', 'Municipality', 'County', 'Number of Completed EE Projects', 'GHG Emissions (MTCO2e)', 'Population (as of 2020)']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle second energy efficiency program POST and serve result web page
@app.route('/ee2_handler', methods=['POST'])
def ee2_handler():
    rows = connect('SELECT mc.municipality_name, mc.county, e.num_ci_taxed_parcels, e.total_completed_projects, e.current_lifetime_rate, e.num_projects_needed FROM municipality_code mc, energy_efficiency_programs e WHERE mc.municipality_index=e.municipality_index;')
    heads = ['Municipality', 'County', 'Number of CI Taxed Parcels', 'Total Number of Compeleted Projects', 'Current Lifetime Rate', 'Number of Projects Needed to get 5%']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle commmunity profile data POST and serve result web page
@app.route('/com_handler', methods=['POST'])
def com_handler():
    rows = connect('SELECT mc.municipality_index, mc.municipality_name, mc.county, c.year, e.total_completed_projects, count(s.application_number), c.median_household_income, c.population FROM municipality_code mc, solar_installation_programs s, community_profile c, energy_efficiency_programs e WHERE c.year=2020 AND e.municipality_index = mc.municipality_index AND s.municipality_index = mc.municipality_index AND c.municipality_index=mc.municipality_index GROUP BY mc.municipality_index, mc.county, c.year, e.total_completed_projects, c.median_household_income, c.population ORDER BY c.'+ request.form['attribute'] +';')
    heads = ['Municipality Index','Municipality', 'County', 'Year', 'Completed Energy Efficiency Projects', '# of Solar Installations', 'Median Household Income', 'Population']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle second commmunity profile data POST and serve result web page
@app.route('/com_handler2', methods=['POST'])
def com_handler2():
    rows = connect('CREATE VIEW mun_elec2 AS SELECT municipality_index, year, residential_electricity, commercial_electricity, industrial_electricity, street_light_electricity FROM municipality; UPDATE mun_elec2 SET residential_electricity=0 WHERE residential_electricity IS NULL; UPDATE mun_elec2 SET commercial_electricity=0 WHERE commercial_electricity IS NULL; UPDATE mun_elec2 SET industrial_electricity=0 WHERE industrial_electricity IS NULL; UPDATE mun_elec2 SET street_light_electricity=0 WHERE street_light_electricity IS NULL; SELECT mc.municipality_name, mc.county, c.year, (m.residential_electricity + m.commercial_electricity + m.industrial_electricity + m.street_light_electricity), g.total_co2, c.median_household_income, c.population FROM municipality_code mc, mun_elec2 m, ghg_emissions g, community_profile c WHERE c.year=2020 AND m.municipality_index = mc.municipality_index AND m.year = c.year AND g.municipality_index = mc.municipality_index AND g.year=c.year AND c.municipality_index = mc.municipality_index ORDER BY c.'+ request.form['attribute'] +';')
    heads = ['Municipality', 'County', 'Year', 'Total Electricity Usage', 'Total CO2 Emissions', 'Median Household Income', 'Population']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle municipality POST and serve result web page
@app.route ('/municipality_handler', methods=['POST'])
def municipality_handler():
    rows = connect('SELECT * FROM municipality_code WHERE municipality_name ILIKE \'%' + request.form['municipality_name'] + '%\';')
    heads = ['Municipality Index', 'Municipality', 'County']
    return render_template('my-result.html', rows=rows, heads=heads)

# handle query POST and serve result web page
@app.route('/query-handler', methods=['POST'])
def query_handler():
    rows = connect(request.form['query'])
    return render_template('my-result.html', rows=rows)

if __name__ == '__main__':
    app.run(debug = True)


