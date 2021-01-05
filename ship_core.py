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
		push_core = "rsync " + "-avzhe ssh $WORKSPACE/BHT-Core/ " + site['user'] + "@" + site['ip'] + ":~/var/www/BHT-Core"
		os.system(push_core)

		# SETUP CORE
		checkout_core = "ssh " + site['user'] + "@" + site['ip'] + " 'cd ~/var/www/BHT-Core; git checkout tags/'" + site['core_tag']
		os.system(checkout_core)		

		with urllib.request.urlopen('http://10.44.0.52/modules/api/?v=record_sites_deployed&result=1&pipeline_name=Xi-Build-Initiator&sid='+site['id']) as response:
			html = response.read()
			
	else:
		with urllib.request.urlopen('http://10.44.0.52/modules/api/?v=record_sites_deployed&result=0&pipeline_name=Xi-Build-Initiator&sid='+site['id']) as response:
			html = response.read()