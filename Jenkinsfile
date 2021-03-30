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
            echo 'Change directory to BHT-EMR-API'
            sh '#cd $WORKSPACE/BHT-EMR-API && git pull origin development'
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
            echo 'Change directory to BHT-Core'
            sh '#cd $WORKSPACE/BHT-Core && git pull origin development'
            echo 'Fetching New Tags'
            sh 'cd $WORKSPACE/BHT-Core && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-Core && git describe $(git describe --tags `git rev-list --tags --max-count=1`)'
          }
        }

        stage('Fetching ART') {
          steps {
            echo 'Starting to fetch ART from GitHub'
            echo 'Checking if BHT-Core-Apps-ART exists.'
            sh '[ -d "BHT-Core-Apps-ART" ] && echo "ART already cloned." || git clone https://github.com/HISMalawi/BHT-Core-Apps-ART.git'
            echo 'Change directory to ART'
            sh '#cd $WORKSPACE/BHT-Core-Apps-ART && git pull origin development'
            echo 'Fetching new tags'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git describe > HEAD'
          }
        }

      }
    }

    stage('Remote checkout to latest tag') {
      parallel {
        stage('API') {
          steps {
            sh '''#Opsuser
#BHT-EMR-API
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-EMR-API && git fetch --tags -f git://10.44.0.51/var/lib/jenkins/workspace/art-setup-no-container_master/BHT-EMR-API\'
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-EMR-API && git checkout v4.10.24\'
rsync -a --exclude \'config\' $WORKSPACE/BHT-EMR-API opsuser@10.44.0.52:/home/opsuser/poc_test/BHT-EMR-API'''
          }
        }

        stage('Core') {
          steps {
            sh '''#Opsuser
#BHT-Core
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core && git fetch --tags -f git://10.44.0.51/var/lib/jenkins/workspace/art-setup-no-container_master/BHT-Core\'
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core && git checkout v4.7.7\''''
          }
        }

        stage('ART') {
          steps {
            sh '''#Opsuser
#BHT-Core
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core/apps/ART && git fetch --tags -f git://10.44.0.51/var/lib/jenkins/workspace/art-setup-no-container_master/BHT-Core-Apps-ART\'
#ssh opsuser@10.44.0.52 \'cd /home/opsuser/poc_test/BHT-Core/apps/ART && git checkout v4.11.1\''''
          }
        }

      }
    }

    stage('Testing') {
      steps {
        echo 'No testing functionality found'
      }
    }

    stage('Shipping') {
      parallel {
        stage('Shipping API') {
          steps {
            echo 'Starting to ship API'
            sh '#python3 ship_api.py'
          }
        }

        stage('Shipping Core') {
          steps {
            echo 'Starting to ship Core'
            sh '#python3 ship_core.py'
          }
        }

        stage('Shipping ART') {
          steps {
            echo 'Starting to ship ART'
            sh '#python3 ship_art.py'
          }
        }

      }
    }

    stage('Setup App') {
      steps {
        echo 'Starting to setup App'
        sh '#python3 data_setup.py'
      }
    }

  }
}