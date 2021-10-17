pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('docker-hubp')
	}

	stages {

		stage('Build') {
                          sh'sudo usermod -a -G docker jenkins'      
			steps {
				
				sh 'docker build -t marwan1408/docker-testtt:latest .'
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
