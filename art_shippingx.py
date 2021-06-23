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

for site_id in all_sites_in_cluster:
    site_endpoint = "http://10.44.0.52/sites/api/v1/get_single_site/" + str(site_id)
    site_req = urllib.request.Request(site_endpoint)
    site_r = urllib.request.urlopen(site_req).read()
    site_details = json.loads(site_r.decode('utf-8'))
    sitex = site_details[0]['fields']

    for site in xi_api['cluster']:
        param = '-n' if platform.system().lower()=='windows' else '-c'
        if subprocess.call(['ping', param, '1', site['ip']]) == 0:
            push_art = "rsync " + "-r ssh $WORKSPACE/BHT-Core/apps-ART/ " + site['user'] + "@" + site['ip'] + ":~/var/www/BHT-Core/apps/ART"
            os.system(push_art)