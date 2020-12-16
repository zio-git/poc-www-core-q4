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
        echo 'Clean up'
        sh '[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git'
        sh 'git tag -l'
      }
    }

    stage('Fetching Core') {
      steps {
        echo 'Cloning ART'
      }
    }

  }
}