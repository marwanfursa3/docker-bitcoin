<<<<<<< HEAD
node{
  
        stage('Clone GitHub Repositry'){
            
                git branch: 'master', url:'https://github.com/marwanfursa3/docker-test.git'
          
         }
        stage('mvn'){
              def mvnHOme= tool name: 'maven3', type: 'maven'
            def mvnCMD = "${mvnHOme}/bin/mvn"
            sh "${mvnCMD} clean package"
          
         }
        stage('build docker image'){
           
              sh 'docker build -t marwan1408/docker-testt:2.0.0 .'
        }
        stage('build docker image'){
           
              sh 'docker build -t marwan1408/docker-testt:2.0.0 .'
        }
        stage('build docker image'){
              withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerhub')]) {
                    sh 'docker login -u marwan1408 -p ${dockerhub}'
              }
    
              sh 'docker push marwan1408/docker-testt:2.0.0'
        }
        stage('run container on dev server'){
              def dockerRun = 'docker run -p 8080:8080 -d --name docker-testt marwan1408/docker-testt:2.0.0'
              sshagent(['7a46fbc7-a25f-4216-ac5d-2b8d22718ab8']) {
                    sh "ssh -o StrictHostKeyChecking=no ubuntu@192.168.1.106 ${dockerRun}"
             }
        }
    }
=======
pipeline {
  environment {
    registry = "marwan1408/docker-testt"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
       git branch: 'master', url:'https://github.com/marwanfursa3/docker-test.git'
    }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
        sh "docker rmi $registry:$BUILD_NUMBER"
      }
    }
  }
}
>>>>>>> 5c9ca7662ae9ae1028ea6acea2825f524861f2d4
