pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Build Container') {
      agent {
        dockerfile {
          filename 'Dockerfile'
        }

      }
      steps {
        container(name: 'build', shell: 'docker build . -t django-test:0.1 --network=host')
      }
    }

  }
}