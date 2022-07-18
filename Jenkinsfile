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
        script {
          docker.withRegistry('10.233.61.130:5000', 'nexus') {
            docker.image('10.233.61.130:5000/django-test:0.13').push()
          }
        }
      }
    }
  }
}
