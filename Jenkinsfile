pipeline {
  agent any
  stages {
    stage('Clone API') {
      steps {
        echo 'Cloning API'
        sh '''git clone https://github.com/HISMalawi/BHT-EMR-API.git .
'''
      }
    }

    stage('Clone Core') {
      steps {
        echo 'Cloning BHT-Core'
        sh 'mkdir BHT-Core'
      }
    }

    stage('Clone ART') {
      steps {
        echo 'Cloning ART'
      }
    }

  }
}