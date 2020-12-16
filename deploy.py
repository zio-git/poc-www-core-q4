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

		# push to site
		#push_to_site = "rsync " + "-avzhe ssh $PWD/ " + site['user'] + "@" + site['ip'] + ":~/devops/poc"
		#os.system(push_to_site)

		# unzip nginx
		#unzip_nginx = "ssh " + site['user'] + "@" + site['ip'] + " 'zcat nginx.gz | docker import - nginx'"
		#os.system(unzip_nginx)

		# unzip bht_emr_api
		#unzip_bht_emr_api = "ssh " + site['user'] + "@" + site['ip'] + " 'zcat bht_emr_api.gz | docker import - bht_emr_api'"
		#os.system(unzip_bht_emr_api)

		# unzip bht_emr_api
		#unzip_nlims_data_syncroniser = "ssh " + site['user'] + "@" + site['ip'] + " 'zcat nlims_data_syncroniser.gz | docker import - nlims_data_syncroniser'"
		#os.system(unzip_nlims_data_syncroniser)

# unzip nlims_controller
		#unzip_nlims_controller = "ssh " + site['user'] + "@" + site['ip'] + " 'zcat nlims_controller.gz | docker import - nlims_controller'"
		#os.system(unzip_nlims_controller)

		# unzip lab_test_controller
		#unzip_lab_test_controller = "ssh " + site['user'] + "@" + site['ip'] + " 'zcat lab_test_controller.gz | docker import - lab_test_controller'"
		#os.system(unzip_lab_test_controller)

		# unzip couchdb
		#unzip_couchdb = "ssh " + site['user'] + "@" + site['ip'] + " 'zcat couchdb.gz | docker import - couchdb'"
		#os.system(unzip_couchdb)

		# unzip mysqldb
		#unzip_mysqldb= "ssh " + site['user'] + "@" + site['ip'] + " 'zcat mysqldb.gz | docker import - mysqldb'"
		#os.system(unzip_mysqldb)

		# docker compose build
		#buildx = "ssh " + site['user'] + "@" + site['ip'] + " 'docker-compose build'"
		#os.system(buildx)

		# docker compose run
		runx = "ssh " + site['user'] + "@" + site['ip'] + " 'cd ~/devops/poc; docker-compose up -d --no-recreate --remove-orphans'"
		os.system(runx)

		with urllib.request.urlopen('http://10.44.0.52/modules/api/?v=record_sites_deployed&result=1&pipeline_name=Xi-Build-Initiator&sid='+site['id']) as response:
			html = response.read()
	else:
		with urllib.request.urlopen('http://10.44.0.52/modules/api/?v=record_sites_deployed&result=0&pipeline_name=Xi-Build-Initiator&sid='+site['id']) as response:
			html = response.read()



