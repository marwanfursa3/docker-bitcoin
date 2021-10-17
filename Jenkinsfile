pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hubp')
	}

	stages {
		stage('Cloning Git') {
                            steps {
                                   git branch: 'master', url:'https://github.com/marwanfursa3/docker-bitcoin.git'
                   }
		}
              //  stage('clone') {
                  
		//	steps {
				
		//	 sh'sudo usermod -a -G docker jenkins'  
		//	}
		//}
		stage('Build') {
                      
			steps {
				
				sh 'sudo docker build -t marwan1408/docker-testtt:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'docker push marwan1408/docker-testt:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
