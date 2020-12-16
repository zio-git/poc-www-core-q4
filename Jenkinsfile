pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing ...'
      }
    }

    stage('Fetch API') {
      steps {
        echo 'Starting to fetch API from GitHub repo'
        echo 'Clean up'
        sh '[ -d "BHT-EMR-API" ] && echo rm -r BHT-EMR-API || echo "No API directory found. Proceeding with installation."'
      }
    }

    stage('Fetch Core') {
      steps {
        echo 'Cloning ART'
      }
    }

  }
}