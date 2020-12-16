pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing ...'
      }
    }

    stage('Fetching API') {
      steps {
        echo 'Starting to fetch API from GitHub repo'
        echo 'Checking if BHT-EMR-API exists.'
        sh '[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git'
        echo 'Change directory to BHT-EMR-API'
        sh 'cd $WORKSPACE/BHT-EMR-API && git pull origin development'
        echo 'Move all new changes to nodes within the cluster'
        sh 'python3 deploy.py'
      }
    }

    stage('Fetching Core') {
      steps {
        echo 'Cloning ART'
      }
    }

  }
}
