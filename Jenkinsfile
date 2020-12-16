pipeline {
  agent any
  stages {
    stage('Initiate') {
      steps {
        echo 'Initiating a build'
        git(branch: 'development', url: 'https://github.com/HISMalawi/BHT-EMR-API.git', credentialsId: 'none', poll: true, changelog: true)
        sh '''#!/bin/sh

#The following will update POC
cd ~

cd /var

localdir="/var/www"

#updating API and checking out to the latest tag
	echo "The API is already installed ... NOW preparing to update !!"
	cd $localdir/BHT-EMR-API
	latesttag=$(git describe --tags)
	repo1= "https://github.com/HISMalawi/BHT-EMR-API.git"
	git pull origin development "$repo1"
  	echo checking out ${latesttag}
        git checkout ${latesttag}
      rails db:migrate
      ./bin/update_art_metadata.sh development

     echo "Api Update successful!! "
#Updating BHT-Core and checking out to the latest tag

  echo "BHT-Core is already installed ... NOW preparing to update !!"
        cd $localdir/BHT-Core
        latesttag=$(git describe --tags)
	repo2="https://github.com/HISMalawi/BHT-Core.git"
	git stash | git pull -f "$repo2" 
        echo checking out ${latesttag}
        git checkout ${latesttag}
        echo $latesttag $localdir/BHT-Core
 
 echo " BHT-Core Update successful!! "

#Updating ART module and checking out to the latest tag

  echo "ART is already installed ... NOW preparing to update !!"
        cd $localdir/BHT-Core/apps/ART
        latesttag=$(git describe --tags)
	repo3="https://github.com/HISMalawi/BHT-Core-Apps-ART.git"
	 git pull -f "$repo3" 

        echo checking out ${latesttag}
        git checkout ${latesttag}
        echo $latesttag $localdir/BHT-Core/apps/ART

echo " ART Update successful!! "

#     Restarting web server
#     cd /var/www/BHT-EMR-API/ | echo 123456 | sudo /opt/nginx/sbin/nginx -s reload'''
      }
    }

    stage('Build') {
      steps {
        echo 'Setting up POC Backend'
      }
    }

  }
}