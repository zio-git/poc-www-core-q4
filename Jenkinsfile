pipeline {
  agent any
  stages {
    stage('Clone API') {
      steps {
        echo 'Cloning API'
        sh '''dir="BHT-EMR-API"
rm -r $dir'''
        sh '''latesttag=$(git describe --tags)
repo1= "https://github.com/HISMalawi/BHT-EMR-API.git"
git pull origin development "$repo1"
git checkout ${latesttag}


    
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