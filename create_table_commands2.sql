CREATE TABLE municipality_code (
PRIMARY KEY (Municipality_index), Municipality_index text,
Municipality_name varchar(30),
County varchar(30));

CREATE TABLE municipality (
Residential_electricity text,
Commercial_electricity text,
Industrial_electricity text,
Street_light_electricity text,
Residential_gas text,
Commercial_gas text,
Industrial_gas text,
Street_light_gas text,
Gas_utility text,
Electric_utility text, 
County varchar(30), 
Year int, Municipality_index text,
PRIMARY KEY (Municipality_index, Year),
FOREIGN KEY (Municipality_index) REFERENCES municipality_code (Municipality_index)
MATCH FULL );

CREATE TABLE energy_efficiency_programs (
Municipality_index text,
Num_CI_taxed_parcels int,
Total_completed_projects int,
current_lifetime_rate float,
Num_projects_needed int,
PRIMARY KEY (Municipality_index),
FOREIGN KEY (Municipality_index) REFERENCES municipality_code (Municipality_index)
MATCH FULL );

CREATE TABLE solar_installation_programs (
Application_number text,
Municipality_index text,
Status text,
Third_party_ownership varchar(3),
Program text, 
PTO_date timestamp,
Calculated_system_size float,
Contractor text, 
Interconnection text,
Utility_name text,
PRIMARY KEY (Application_number),
FOREIGN KEY (Municipality_index) REFERENCES municipality_code (Municipality_index)
MATCH FULL );

CREATE TABLE ghg_emissions(
Municipality_index int,
Year int,
Total_co2 int,
PRIMARY KEY (Municipality_index, Year),
FOREIGN KEY (Municipality_index) REFERENCES municipality_code(municipality_index)
MATCH FULL );

CREATE TABLE commercial_solar_customer (
Application_number text,
Premise_company text,
premise_installation_address text,
PRIMARY KEY (Application_number),
FOREIGN KEY (Application_number) REFERENCES solar_installation_programs (Application_number)
MATCH FULL );
