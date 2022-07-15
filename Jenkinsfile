pipeline {
  agent {
    node {
      label 'docker'
    }
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
