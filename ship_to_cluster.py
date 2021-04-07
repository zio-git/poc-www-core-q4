import os
import platform
import subprocess
import utils

cluster_endpoint = 'http://10.44.0.52/sites/api/v1/get_single_cluster/1'
site_endpoint = 'http://10.44.0.52/sites/api/v1/get_single_site/'



for site in utils.api.get_sites_from_cluster(cluster_endpoint, site_endpoint):    
    
    for fetched_site in utils.api.get_site(site, site_endpoint):

        if utils.net.ping(fetched_site['fields']['ip_address']):

            if utils.files.push('api', fetched_site['fields']['username'], fetched_site['fields']['ip_address']):

                print("Files pushed successfully.")

            else:

                print("Failed to transfer.")