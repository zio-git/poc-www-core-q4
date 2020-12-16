pipeline {
  agent any
  stages {
    stage('Clone API') {
      steps {
        echo 'Cloning API'
        sh '''mkdir BHT-EMR-API
'''
        git(url: 'https://github.com/HISMalawi/BHT-EMR-API.git', changelog: true, poll: true)
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