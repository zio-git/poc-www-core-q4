pipeline {
  agent any
  stages {
    stage('Initiate') {
      steps {
        echo 'Initiating a build'
        git(branch: 'development', url: 'https://github.com/HISMalawi/BHT-EMR-API.git', credentialsId: 'none', poll: true, changelog: true)
      }
    }

    stage('Checkout') {
      steps {
        dir(path: '/var/www/BHT-EMR-API')
      }
    }

    stage('Migration') {
      steps {
        echo 'Run migrations'
      }
    }

  }
}