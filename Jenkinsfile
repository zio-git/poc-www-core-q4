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
            echo 'Giving access to all users'
            sh 'cd $WORKSPACE && chmod 777 BHT-EMR-API'
            echo 'Fetching Tags'
            sh 'cd $WORKSPACE/BHT-EMR-API && git fetch --tags -f'
            echo 'Checking out to Latest Tag'
            sh 'cd $WORKSPACE/BHT-EMR-API && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-EMR-API && git describe > HEAD'
          }
        }

        stage('Fetching Core') {
          steps {
            echo 'Starting to fetch Core from GitHub'
            echo 'Checking if BHT-Core exists.'
            sh '[ -d "BHT-Core" ] && echo "Core already cloned." || git clone https://github.com/HISMalawi/BHT-Core.git'
            echo 'Giving access to users'
            sh 'cd $WORKSPACE && chmod 777 BHT-Core'
            echo 'Fetching New Tags'
            sh 'cd $WORKSPACE/BHT-Core && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/BHT-Core && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/BHT-Core && git describe $(git describe --tags `git rev-list --tags --max-count=1`)'
          }
        }

        stage('Fetching ART') {
          steps {
            echo 'Starting to fetch ART from GitHub'
            echo 'Checking if BHT-Core-Apps-ART exists.'
            sh '[ -d "ART" ] && echo "ART already cloned." || git clone https://github.com/HISMalawi/BHT-Core-Apps-ART.git ART'
            echo 'Giving access to all user'
            sh 'cd $WORKSPACE && chmod 777 ART'
            echo 'Fetching new tags'
            sh 'cd $WORKSPACE/ART && git fetch --tags -f'
            echo 'Checking out to latest tag'
            sh 'cd $WORKSPACE/ART && git checkout $(git describe --tags `git rev-list --tags --max-count=1`)'
            sh 'cd $WORKSPACE/ART && git describe > HEAD'
          }
        }

      }
    }

    stage('Shipping & configuring') {
      parallel {
        stage('API') {
          steps {
            sh 'python3 cluster_manager.py'
          }
        }

        stage('Core') {
          steps {
            echo 'Copying and configuring API'
          }
        }

      }
    }

    stage('Apps') {
      parallel {
        stage('ART') {
          steps {
            echo 'Copying & configuring ART'
          }
        }

        stage('OPD') {
          steps {
            echo 'Checking if OPD is deployed on new architecture'
          }
        }

        stage('ANC') {
          steps {
            echo 'Checking if ANC is deployed on new architecture'
          }
        }

        stage('TB') {
          steps {
            echo 'Checking if TB is deployed on new architecture'
          }
        }

        stage('HTS') {
          steps {
            echo 'Checking if HTS is deployed on new architecture'
          }
        }

      }
    }

    stage('Loading metadata') {
      steps {
        echo 'Loading metadata'
      }
    }

  }
}