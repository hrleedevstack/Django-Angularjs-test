pipeline {
  agent any
  stages {
    stage('Build Container') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        container(name: 'build')
      }
    }

  }
}