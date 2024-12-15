Psycopg2 para Macc y Linux:
sudo apt install python3-dev libpq-dev

Cuando se instalan los requerimientos si usa python 3.10 da un error y hay que poner en requirements.txt quitar "backports.zoneinfo==0.2.1" y poner : " backports.zoneinfo==0.2.1;python_version<"3.9" " porque da un error con la version mas actual.
