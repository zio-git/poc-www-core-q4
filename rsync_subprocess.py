source_dir = "$WORKSPACE/BHT-EMR-API/"

destination_dir = username + "@" + ip + ":/var/www/BHT-EMR-API"

result = subprocess.call(['rsync', '--exclude=config', '-avzhe',  'ssh', source_dir, destination_dir])