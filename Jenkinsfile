// pipeline {
//   agent {
//     dockerfile {
//       filename 'Dockerfile'
//     }

//   }
//   stages {
//     stage('Build Container') {
//       agent {
//         dockerfile {
//           filename 'Dockerfile'
//           additionalBuildArgs '-t django-test:0.11 --network=host'
//         }

//       }
//     }

//   }
// }

pipeline {
  agent any
  stages {
    stage('Example') {
      steps {
        echo 'Hello, World!'
      }
    }
  }
}