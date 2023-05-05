#psql -u lion -p cab12 < \i deleteOldTables.sql

#psql -u lion -p cab12 < \i create_table_commands2.sql
sh vm_setup.sh

createdb cab12

python install_databases.py

#psql -u lion -p cab12 < \i updateMunicipality.sql
