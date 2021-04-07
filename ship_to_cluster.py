import os
import platform
import subprocess
import utils

cluster_endpoint = 'http://10.44.0.52/sites/api/v1/get_single_cluster/1'
site_endpoint = 'http://10.44.0.52/sites/api/v1/get_single_site/'



for site in utils.api.get_sites_from_cluster(cluster_endpoint, site_endpoint):    
    
    for fetched_site in utils.api.get_site(site, site_endpoint):

        if utils.net.ping(fetched_site['fields']['ip_address']):

            apps = ['api', 'core', 'art']

            for app in apps:

                if utils.files.push(app, fetched_site['fields']['username'], fetched_site['fields']['ip_address']):

                    print("Files pushed successfully.")
                    # load meta data
                    # change app version/tag
                    # change status on Xi to depict successful transfer of files to site
                    # send email alert to followers or maybe generate report

                else:

                    print("Failed to transfer.")
                    # change status on Xi to depict failed transfer of files
                    # send email alert to followers or maybe generate report