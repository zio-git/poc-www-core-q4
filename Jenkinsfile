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
        echo 'Starting to fetch API from GitHub'
        echo 'Checking if BHT-EMR-API exists.'
        sh '[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git'
        echo 'Change directory to BHT-EMR-API'
        sh 'cd $WORKSPACE/BHT-EMR-API && git pull origin development'
        echo 'All changes up-to-date. Ready to ship to sites.'
      }
    }

    stage('Fetching Core') {
      steps {
        echo 'Starting to fetch Core from GitHub'
        echo 'Checking if BHT-Core exists.'
        sh '[ -d "BHT-Core" ] && echo "Core already cloned." || git clone https://github.com/HISMalawi/BHT-Core.git'
        echo 'Change directory to BHT-Core'
        sh 'cd $WORKSPACE/BHT-Core && git pull origin development'
        echo 'All changes up-to-date. Ready to ship to sites.'
      }
    }

    stage('Fetching ART') {
      steps {
        echo 'Starting to fetch ART from GitHub'
        echo 'Checking if BHT-Core-Apps-ART exists.'
        sh '[ -d "BHT-Core-Apps-ART" ] && echo "ART already cloned." || git clone https://github.com/HISMalawi/BHT-Core-Apps-ART.git'
        echo 'Change directory to ART'
        sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git pull origin development'
        echo 'All changes up-to-date. Ready to ship to sites.'
      }
    }
    
    stage('Building App') {
      steps {
        echo 'Starting to build the App'
      }
    }
    
    stage('Testing') {
      steps {
        echo 'No testing functionality found'
      }
    }
    
    stage('Shipping') {
      steps {
        echo 'Starting to ship to sites'
      }
    }

  }
}
