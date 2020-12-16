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
        sh '[ -d "BHT-EMR-API" ] && rm -r BHT-EMR-API || echo "No API directory found. Proceeding to fetch repository."'
        sh 'git clone https://github.com/HISMalawi/BHT-EMR-API.git'
        sh 'git fetch --tags --force --progress -- https://github.com/HISMalawi/BHT-EMR-API.git +refs/heads/*:refs/remotes/origin/*'
      }
    }

    stage('Fetching Core') {
      steps {
        echo 'Cloning ART'
      }
    }

  }
}