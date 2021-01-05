import os
import urllib.request
import json
import platform
import subprocess

# define URL to capture data
url = 'http://10.44.0.52/modules/api/?v=cluster&pipeline_name=Xi-Build-Initiator'
req = urllib.request.Request(url)

# parsing response
r = urllib.request.urlopen(req).read()
xi_api = json.loads(r.decode('utf-8'))

for site in xi_api['cluster']:	

	param = '-n' if platform.system().lower()=='windows' else '-c'

	if subprocess.call(['ping', param, '1', site['ip']]) == 0:

		# PUSH CORE
		db_import_1 = "ssh " + site['user'] + "@" + site['ip'] + " 'cd $WORKSPACE/BHT-EMR-API; mysql -uroot -proot openmrs < db/sql/openmrs_metadata_1_7.sql -v -f'"
		os.system(db_import_1)	

		db_import_2 = "ssh " + site['user'] + "@" + site['ip'] + " 'cd $WORKSPACE/BHT-EMR-API; mysql -uroot -proot openmrs < db/sql/alternative_drug_names.sql -v -f'"
		os.system(db_import_2)

		db_import_3 = "ssh " + site['user'] + "@" + site['ip'] + " 'cd $WORKSPACE/BHT-EMR-API; mysql -uroot -proot openmrs < moh_regimens_v2020.sql -v -f'"
		os.system(db_import_3)

		db_import_4 = "ssh " + site['user'] + "@" + site['ip'] + " 'cd $WORKSPACE/BHT-EMR-API; mysql -uroot -proot openmrs < bart2_views_schema_additions.sql -v -f'"
		os.system(db_import_4)


		migrations = "ssh " + site['user'] + "@" + site['ip'] + " 'cd $WORKSPACE/BHT-EMR-API; rake db:migrate'"
		os.system(migrations)



		with urllib.request.urlopen('http://10.44.0.52/modules/api/?v=record_sites_deployed&result=1&pipeline_name=Xi-Build-Initiator&sid='+site['id']) as response:
			html = response.read()
			
	else:
		with urllib.request.urlopen('http://10.44.0.52/modules/api/?v=record_sites_deployed&result=0&pipeline_name=Xi-Build-Initiator&sid='+site['id']) as response:
			html = response.read()