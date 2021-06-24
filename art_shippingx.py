import requests
import json
import platform
import subprocess
import os

def get_xi_data(url):
    response = requests.get(url)
    data = json.loads(response.text)
    data = data[0]['fields']
    return data

cluster = get_xi_data('http://10.44.0.52/sites/api/v1/get_single_cluster/3')

for site_id in cluster['site']:
    site = get_xi_data('http://10.44.0.52/sites/api/v1/get_single_site/' + str(site_id))

    # lets check if the site is available
    param = '-n' if platform.system().lower()=='windows' else '-c'
    if subprocess.call(['ping', param, '1', site['ip_address']]) == 0:
        
        # ship data to remote site
        push_art = "rsync " + "-r ssh $WORKSPACE/BHT-Core/apps-ART/ " + site['user'] + "@" + site['ip'] + ":~/var/www/BHT-Core/apps/ART"
        os.system(push_art)






