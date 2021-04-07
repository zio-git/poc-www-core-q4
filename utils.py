import os
import urllib.request
import json
import platform
import subprocess
import sys

class api:

    def get_sites_from_cluster(cluster_endpoint, site_endpoint):

        for cluster in json.loads(urllib.request.urlopen(urllib.request.Request(cluster_endpoint)).read().decode('utf-8')):

            return cluster['fields']['site']

    def get_site(site_id, site_endpoint):
        return json.loads(urllib.request.urlopen(urllib.request.Request(site_endpoint + str(site_id))).read().decode('utf-8'))

class net:

    def ping(ip_address):
        
        param = '-n' if platform.system().lower()=='windows' else '-c'

        if subprocess.call(['ping', param, '1', ip_address]) == 0:

            return True

        else:

            return False
            
class files:

    def push(app, username, ip):

        if app == 'api':  

            source_dir = "$WORKSPACE/BHT-EMR-API/"

            destination_dir = username + "@" + ip + ":/var/www/BHT-EMR-API"

            result = subprocess.call(['rsync', '--exclude=config', '-avzhe',  'ssh', source_dir, destination_dir])

            if result == 0:

                return True

            else:

                return False


