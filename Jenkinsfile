pipeline {
	agent any 
	environment {
		DOCKERHUB_CREDENTIAL = credentials('dockerhub-creds')
		DOCKER_IMAGE = 'vyankatesh23/fasttrack-shipment-app'
	}
	
	stages {
		stage ('checkout') {
			steps {
				checkout scm
				}
			}

		stage ('install dependencies') {
			steps {
				sh 'pip install -r requirements.txt --break-system-packages'
				}
			}
		
		stage ('Run test') {
			steps {
				sh 'pytest'
				}
			}
	
		stage ('Dockerhub login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIAL_PSW | docker login -u $DOCKERHUB_CREDENTIAL_USR --password-stdin'
				}
			}
	
		stage ('Build Image') {
			steps {
				sh 'docker build -t $DOCKER_IMAGE:latest .'
				sh 'docker tag $DOCKER_IMAGE:latest $DOCKER_IMAGE:$GIT_COMMIT '
				}
			}

		stage ('Push to Dockerhub') {
			steps {
				sh 'docker push $DOCKER_IMAGE:latest'
				sh 'docker push $DOCKER_IMAGE:$GIT_COMMIT'
				}
			}
		}

	post {
		success {
			echo 'Pipeline completed successfully'
			}
		failure {
			echo 'Pipeline failed check the logs.'
			}
		}
	}

