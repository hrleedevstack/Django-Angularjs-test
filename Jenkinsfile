pipeline {
  agent none
  stages {
    stage('checkout') {
      steps {
        checkout scm
      }
    }
    stage('container build') {
      agent{
        dockerfile {
          additionalBuildArgs '-t 10.233.61.130:5000/django-test:0.12 --network=host'
        }
      }
    }
    stage('contaienr push') {
      agent any
      steps {
        sh 'docker login -u admin -p devstack'
        sh 'docker push 10.233.61.130:5000/django-test:0.12'
      }
    }
  }
}
