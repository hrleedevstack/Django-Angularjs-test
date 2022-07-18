pipeline {
  agent {
    none
  }
  stages {
    stage('build') {
      agent any
      steps {
        sh 'docker build . -t django-test:0.1 --network=host'
      }
    }
  }
}
