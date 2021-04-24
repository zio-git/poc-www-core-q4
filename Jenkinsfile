pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing ...'
        sh 'echo "Working from $WORKSPACE"'
      }
    }

    stage('Fetching Repos') {
      parallel {
        stage('Fetching API') {
          steps {
            echo 'Starting to fetch API from GitHub'
            echo 'Checking if BHT-EMR-API exists.'
            sh '[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git'
            echo 'Giving access to all users'
            sh 'cd $WORKSPACE && chmod 777 BHT-EMR-API'
            echo 'Fetching Tags'
            sh 'cd $WORKSPACE/BHT-EMR-API && git fetch --tags -f'
            echo 'Checking out to Latest Tag'
            sh 'cd $WORKSPACE/BHT-EMR-API && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-EMR-API && git describe > HEAD'
          }
        }

        stage('Fetching Core') {
          steps {
            echo 'Starting to fetch Core from GitHub'
            echo 'Checking if BHT-Core exists.'
            sh '[ -d "BHT-Core" ] && echo "Core already cloned." || git clone https://github.com/HISMalawi/BHT-Core.git'
            echo 'Giving access to users'
            sh 'cd $WORKSPACE && chmod 777 BHT-Core'
            echo 'Fetching New Tags'
            sh 'cd $WORKSPACE/BHT-Core && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-Core && git describe $(git describe --tags `git rev-list --tags --max-count=1`)'
            echo 'Checking/Creating apps folder'
            sh '[ -d "BHT-Core/apps" ] && echo "apps already created." || mkdir apps'
            echo 'Giving access rights to apps'
            sh 'cd $WORKSPACE/BHT-Core && chmod 777 apps'
          }
        }

      }
    }

    stage('Fetching ART') {
      steps {
        echo 'Starting to fetch ART from GitHub'
        echo 'Checking if BHT-Core-Apps-ART exists.'
        sh '[ -d "BHT-Core/apps/ART" ] && echo "ART already cloned." || git clone https://github.com/HISMalawi/BHT-Core-Apps-ART.git ART'
        echo 'Giving access to all user'
        sh 'cd $WORKSPACE/BHT-Core/apps && chmod 777 ART'
        echo 'Fetching new tags'
        sh 'cd $WORKSPACE/BHT-Core/apps/ART && git fetch --tags -f'
        echo 'Checking out to latest tag'
        sh 'cd $WORKSPACE/BHT-Core/apps/ART && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
        sh 'cd $WORKSPACE/BHT-Core/apps/ART && git describe > HEAD'
      }
    }

    stage('Remote Server Backup') {
      steps {
        echo 'Remote Server apps backup'
        sh '''#Mzuzu Macro
#ssh linserver@10.40.30.3 \'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\'
#ssh linserver@10.40.30.3 \'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\'
#ssh linserver@10.40.30.3 \'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/html/BHT-Core/ /var/www/Apps_Backup\'

#Chitipa DHO
#ssh linserver@10.40.22.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.22.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.22.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Karonga DHO
#ssh linserver@10.40.26.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.26.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.26.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Dowa DHO
#ssh meduser@10.41.172.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.41.172.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.41.172.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Rumphi DHO
#ssh linserver@10.2.12.10 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.2.12.10 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.2.12.10 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Chintheche Rural Hospital
#ssh linserver@10.40.51.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.51.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.51.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Kasungu DHO
#ssh meduser@10.41.156.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.41.156.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.41.156.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Nkhotakota DHO
#ssh meduser@10.40.8.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.40.8.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.40.8.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Salima DHO
#ssh meduser@10.41.154.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh meduser@10.41.154.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh meduser@10.41.154.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\'

#Mzuzu Central
#ssh linserver@10.40.11.3 \\\'[ -d "/var/www/Apps_Backup" ] && echo "Directory already exists" || cd /var/www/ && mkdir Apps_Backup\\\'
#ssh linserver@10.40.11.3 \\\'[ -d "/var/www/Apps_Backup/BHT-EMR-API" ] && echo "Directory already exists" || mv /var/www/BHT-EMR-API/ /var/www/Apps_Backup\\\'
#ssh linserver@10.40.11.3 \\\'[ -d "/var/www/Apps_Backup/BHT-Core" ] && echo "Directory already exists" || mv /var/www/BHT-Core/ /var/www/Apps_Backup\\\''''
      }
    }

    stage('Shipping & Configurations') {
      parallel {
        stage('API') {
          steps {
            echo 'shipping & Configuring API'
            sh '''#Mzuzu Macro
#rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.30.3:/var/www
#ssh linserver@10.40.30.3 \'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\'
#ssh linserver@10.40.30.3 \'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\'
#ssh linserver@10.40.30.3 \'cd /var/www/BHT-EMR-API && rvm use 2.5.3\'

#Chitipa DHO
#rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.22.3:/var/www
#ssh linserver@10.40.22.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.22.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.22.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Karonga DHO
#rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.26.3:/var/www
#ssh linserver@10.40.26.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.26.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.26.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Kaporo Rural Hospital
rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.63.3:/var/www
ssh linserver@10.40.63.3 \'cp /var/www/app-backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\'
ssh linserver@10.40.63.3 \'cp /var/www/app-backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\'

#Chilumba Rural Hospital
rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.59.3:/var/www
ssh linserver@10.40.59.3 \'cp /var/www/app-backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\'
ssh linserver@10.40.59.3 \'cp /var/www/app-backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\'

#Madisi Mission Hospital
rsync -a $WORKSPACE/BHT-EMR-API meduser@10.41.173.3:/var/www
ssh meduser@10.41.173.3 \'cp /var/www/app-backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\'
ssh meduser@10.41.173.3 \'cp /var/www/app-backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\'

#Dowa DHO
#rsync -a $WORKSPACE/BHT-EMR-API meduser@10.41.172.3:/var/www
#ssh meduser@10.41.172.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.41.172.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.41.172.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Rumphi DHO
#rsync -a $WORKSPACE/BHT-EMR-API linserver@10.2.12.10:/var/www
#ssh linserver@10.2.12.10 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.2.12.10 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.2.12.10 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Chintheche Rural Hospital
#rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.51.3:/var/www
#ssh linserver@10.40.51.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.51.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.51.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Kasungu DHO
#rsync -a $WORKSPACE/BHT-EMR-API meduser@10.41.156.3:/var/www
#ssh meduser@10.41.156.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.41.156.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.41.156.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Nkhotakota DHO
rsync -a $WORKSPACE/BHT-EMR-API meduser@10.40.8.3:/var/www
#ssh meduser@10.40.8.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.40.8.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.40.8.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Salima DHO
#rsync -a $WORKSPACE/BHT-EMR-API meduser@10.41.154.3:/var/www
#ssh meduser@10.41.154.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.41.154.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh meduser@10.41.154.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\'

#Mzuzu Central
#rsync -a $WORKSPACE/BHT-EMR-API linserver@10.40.11.3:/var/www
#ssh linserver@10.40.11.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/application.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.11.3 \\\'cp /var/www/Apps_Backup/BHT-EMR-API/config/database.yml /var/www/BHT-EMR-API/config\\\'
#ssh linserver@10.40.11.3 \\\'cd /var/www/BHT-EMR-API && rvm use 2.5.3\\\''''
          }
        }

        stage('Core & ART') {
          steps {
            echo 'Shipping & configuring Core & ART'
            sh '''#Mzuzu Macro
#rsync -a $WORKSPACE/BHT-Core linserver@10.40.30.3:/var/www/html
#ssh linserver@10.40.30.3 \'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/html/BHT-Core/config\'
#ssh linserver@10.40.30.3 \'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/html/BHT-Core/config\'
#ssh linserver@10.40.30.3 \'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/html/BHT-Core/public\'
#ssh linserver@10.40.30.3 \'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/html/BHT-Core/apps/ART\'
#ssh linserver@10.40.30.3 \'cd /var/www/html/BHT-Core && rvm use 2.5.3\'
#ssh linserver@10.40.30.3 \'cd /var/www/html/BHT-Core/apps/ART && rvm use 2.5.3\'

#Chitipa DHO
#rsync -a $WORKSPACE/BHT-Core linserver@10.40.22.3:/var/www
#ssh linserver@10.40.22.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.22.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.22.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh linserver@10.40.22.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh linserver@10.40.22.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh linserver@10.40.22.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Karonga DHO
#rsync -a $WORKSPACE/BHT-Core linserver@10.40.26.3:/var/www
#ssh linserver@10.40.26.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.26.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.26.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh linserver@10.40.26.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh linserver@10.40.26.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh linserver@10.40.26.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Kaporo Rural Hospital
rsync -a $WORKSPACE/BHT-Core linserver@10.40.63.3:/var/www/html
ssh linserver@10.40.63.3 \'cp /var/www/html/BHT-Core/config/administration.json.example /var/www/html/BHT-Core/config/administration.json\'
ssh linserver@10.40.63.3 \'cp /var/www/html/BHT-Core/config/config.json.example /var/www/html/BHT-Core/config/config.json\'
ssh linserver@10.40.63.3 \'cp /var/www/app-backup/BHT-Core/public/touchscreentoolkit /var/html/www/BHT-Core/public\'
ssh linserver@10.40.63.3 \'cp /var/www/html/BHT-Core/apps/ART/application.json.example /var/www/html/BHT-Core/apps/ART/application.json\'

#Chilumba Rural Hospital
rsync -a $WORKSPACE/BHT-Core linserver@10.40.59.3:/var/www/html
ssh linserver@10.40.59.3 \'cp /var/www/html/BHT-Core/config/administration.json.example /var/www/html/BHT-Core/config/administration.json\'
ssh linserver@10.40.59.3 \'cp /var/www/html/BHT-Core/config/config.json.example /var/www/html/BHT-Core/config/config.json\'
ssh linserver@10.40.59.3 \'cp /var/www/app-backup/BHT-Core/public/touchscreentoolkit /var/www/html/BHT-Core/public\'
ssh linserver@10.40.59.3 \'cp /var/www/html/BHT-Core/apps/ART/application.json.example /var/www/html/BHT-Core/apps/ART/application.json\'

#Madisi Mission Hospital
rsync -a $WORKSPACE/BHT-Core meduser@10.41.173.3:/var/www
ssh meduser@10.41.173.3 \'cp /var/www/BHT-Core/config/administration.json.example /var/www/BHT-Core/config/administration.json\'
ssh meduser@10.41.173.3 \'cp /var/www/BHT-Core/config/config.json.example /var/www/BHT-Core/config/config.json\'
ssh meduser@10.41.173.3 \'cp /var/www/app-backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\'
ssh meduser@10.41.173.3 \'cp /var/www/BHT-Core/apps/ART/application.json.example /var/www/BHT-Core/apps/ART/application.json\'

#Dowa DHO
#rsync -a $WORKSPACE/BHT-Core meduser@10.41.172.3:/var/www
#ssh meduser@10.41.172.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.41.172.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.41.172.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh meduser@10.41.172.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh meduser@10.41.172.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh meduser@10.41.172.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Rumphi DHO
#rsync -a $WORKSPACE/BHT-Core linserver@10.2.12.10:/var/www
#ssh linserver@10.2.12.10 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.2.12.10 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.2.12.10 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh linserver@10.2.12.10 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh linserver@10.2.12.10 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh linserver@10.2.12.10 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Chintheche Rural Hospital
#rsync -a $WORKSPACE/BHT-Core linserver@10.40.51.3:/var/www/html
#ssh linserver@10.40.51.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.51.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.51.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh linserver@10.40.51.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh linserver@10.40.51.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh linserver@10.40.51.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Kasungu DHO
#rsync -a $WORKSPACE/BHT-Core meduser@10.41.156.3:/var/www
#ssh meduser@10.41.156.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.41.156.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.41.156.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh meduser@10.41.156.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh meduser@10.41.156.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh meduser@10.41.156.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'


#Nkhotakota DHO
rsync -a $WORKSPACE/BHT-Core meduser@10.40.8.3:/var/www
#ssh meduser@10.40.8.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.40.8.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.40.8.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh meduser@10.40.8.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh meduser@10.40.8.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh meduser@10.40.8.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Salima DHO
#rsync -a $WORKSPACE/BHT-Core meduser@10.41.154.3:/var/www
#ssh meduser@10.41.154.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.41.154.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh meduser@10.41.154.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh meduser@10.41.154.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh meduser@10.41.154.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh meduser@10.41.154.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'

#Mzuzu Central
#rsync -a $WORKSPACE/BHT-Core linserver@10.40.11.3:/var/www
#ssh linserver@10.40.11.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/administration.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.11.3 \\\'cp /var/www/Apps_Backup/BHT-Core/config/config.json /var/www/BHT-Core/config\\\'
#ssh linserver@10.40.11.3 \\\'cp /var/www/Apps_Backup/BHT-Core/public/touchscreentoolkit /var/www/BHT-Core/public\\\'
#ssh linserver@10.40.11.3 \\\'cp /var/www/Apps_Backup/BHT-Core/apps/ART/application.json /var/www/BHT-Core/apps/ART\\\'
#ssh linserver@10.40.11.3 \\\'cd /var/www/BHT-Core && rvm use 2.5.3\\\'
#ssh linserver@10.40.11.3 \\\'cd /var/www/BHT-Core/apps/ART && rvm use 2.5.3\\\'
'''
          }
        }

      }
    }

    stage('Apps') {
      steps {
        echo 'Copying OPD/ANC/HTS if it was deployed on new architecture'
        sh '''#Mzuzu Macro
#ssh linserver@10.40.30.3 \'[ -d "/var/www/Apps_Backup/BHT-Core/apps/OPD" ] && cp /var/www/Apps_Backup/BHT-Core/apps/OPD /var/www/html/BHT-Core/apps || echo "Directory does not exist\'
#ssh linserver@10.40.30.3 \'[ -d "/var/www/Apps_Backup/BHT-Core/apps/HTS" ] && cp /var/www/Apps_Backup/BHT-Core/apps/HTS /var/www/html/BHT-Core/apps || echo "Directory does not exist\'
#ssh linserver@10.40.30.3 \'[ -d "/var/www/Apps_Backup/BHT-Core/apps/ANC" ] && cp /var/www/Apps_Backup/BHT-Core/apps/ANC /var/www/html/BHT-Core/apps || echo "Directory does not exist\''''
      }
    }

    stage('Lading Metadata') {
      steps {
        echo 'Loading metadata'
        sh '''#Mzuzu Macro
#ssh linserver@10.40.30.3 \'cd /var/www/BHT-EMR-API && mysql -uroot -proot macro_mzuzu_openmrs < db/sql/bart2_views_schema_additions.sql\'
'''
      }
    }

  }
}