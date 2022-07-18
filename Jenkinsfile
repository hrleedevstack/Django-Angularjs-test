pipeline {
  agent {
    none
  }
  stages {
    stage('build') {
      agent any
      steps {
        sh 'docker build . -t 10.233.61.130:5000/django-test:0.11 --network=host'
      }
    }
    stage('push') {
      agent any
      steps {
        sh 'docker push 10.233.61.130:5000/django-test:0.1'
      }
    }
  }
}
