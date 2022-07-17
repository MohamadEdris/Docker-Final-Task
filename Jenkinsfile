pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('mohamad-edris')
	}

	stages {

		stage('Build') {

			steps {
				sh 'sudo docker build -t medris2796/bitcoin-final-task:latest .'
			}
		}

		stage('Login') {

			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {

			steps {
				sh 'sudo docker push medris2796/bitcoin-final-task:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}
