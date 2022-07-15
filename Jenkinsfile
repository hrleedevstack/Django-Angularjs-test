pipeline {
  agent {
    dockerfile true

  }
  stages {
    stage ('checlout code') {
      steps {
        checkout scm
      }
    }
    stage ('verify tools'){
      steps {
        sh "docker -v"
      }
    }
  }
}
