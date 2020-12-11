pipeline {
  agent any
  stages {
    stage('Initiate') {
      steps {
        echo 'Initiating a build'
        git(branch: 'development', url: 'https://github.com/HISMalawi/BHT-EMR-API.git', credentialsId: 'none', poll: true, changelog: true)
      }
    }

    stage('Fetch code') {
      steps {
        git(url: 'https://github.com/HISMalawi/BHT-EMR-API.git', branch: 'development', changelog: true, poll: true, credentialsId: 'none')
      }
    }

  }
}