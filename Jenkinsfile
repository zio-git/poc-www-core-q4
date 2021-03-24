pipeline {
  agent any
  stages {
    stage('Initializing') {
      steps {
        echo 'Initializing ...'
        sh 'echo "Working from $WORKSPACE"'
      }
    }

    stage('Fetching Repos') {
      parallel {
        stage('Fetching API') {
          steps {
            echo 'Starting to fetch API from GitHub'
            echo 'Checking if BHT-EMR-API exists.'
            sh '[ -d "BHT-EMR-API" ] && echo "API already cloned." || git clone https://github.com/HISMalawi/BHT-EMR-API.git'
            echo 'Change directory to BHT-EMR-API'
            sh 'cd $WORKSPACE/BHT-EMR-API && git pull origin development'
            echo 'Fetching Tags'
            sh 'cd $WORKSPACE/BHT-EMR-API && git fetch --tags -f'
            echo 'Checking out to Latest Tag'
            sh 'cd $WORKSPACE/BHT-EMR-API && latestTag=$(git describe --tags `git rev-list --tags --max-count=1`) && git checkout $latesttag'
            sh 'cd $WORKSPACE/BHT-EMR-API && git describe > HEAD'
          }
        }

        stage('Fetching Core') {
          steps {
            echo 'Starting to fetch Core from GitHub'
            echo 'Checking if BHT-Core exists.'
            sh '[ -d "BHT-Core" ] && echo "Core already cloned." || git clone https://github.com/HISMalawi/BHT-Core.git'
            echo 'Change directory to BHT-Core'
            sh 'cd $WORKSPACE/BHT-Core && git pull origin development'
            echo 'Fetching New Tags'
            sh 'cd $WORKSPACE/BHT-Core && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core && latestTag=$(git describe --tags `git rev-list --tags --max-count=1`) && git checkout $latesttag'
            sh 'cd $WORKSPACE/BHT-Core && git describe > HEAD'
          }
        }

        stage('Fetching ART') {
          steps {
            echo 'Starting to fetch ART from GitHub'
            echo 'Checking if BHT-Core-Apps-ART exists.'
            sh '[ -d "BHT-Core-Apps-ART" ] && echo "ART already cloned." || git clone https://github.com/HISMalawi/BHT-Core-Apps-ART.git'
            echo 'Change directory to ART'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git pull origin development'
            echo 'Fetching new tags'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && latestTag=$(git describe --tags `git rev-list --tags --max-count=1`) && git checkout $latesttag'
            sh 'cd $WORKSPACE/BHT-Core-Apps-ART && git describe > HEAD'
          }
        }

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
      parallel {
        stage('Shipping API') {
          steps {
            echo 'Starting to ship API'
            sh '#python3 ship_api.py'
          }
        }

        stage('Shipping Core') {
          steps {
            echo 'Starting to ship Core'
            sh '#python3 ship_core.py'
          }
        }

        stage('Shipping ART') {
          steps {
            echo 'Starting to ship ART'
            sh '#python3 ship_art.py'
          }
        }

      }
    }

    stage('Setup App') {
      steps {
        echo 'Starting to setup App'
        sh '#python3 data_setup.py'
      }
    }

  }
}