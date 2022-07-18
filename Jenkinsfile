pipeline {
  agent none
  stages {
    stage('checkout') {
      agent any
      steps {
        checkout scm
      }
    }
    stage('container build') {
      agent{
        dockerfile {
          additionalBuildArgs '-t 10.233.61.130:5000/django-test:0.13 --network=host'
        }
      }
      steps {
        echo 'build container done'
      }
    }
    stage('container push') {
      agent any
      steps {
        sh 'docker login -u admin -p devstack'
        sh 'docker push 10.233.61.130:5000/django-test:0.13'
      }
    }
  }
}
