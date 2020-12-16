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
        sh 'cd BHT-EMR-API'
        echo 'Pull all latest changes for BHT-EMR-API'
        sh 'git pull origin development'
      }
    }

    stage('Fetching Core') {
      steps {
        echo 'Cloning ART'
      }
    }

  }
}
