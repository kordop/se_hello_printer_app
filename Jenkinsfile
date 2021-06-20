pipeline {
    agent any
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3.6'
                    reuseNode true
                }
            }
            steps {
                sh 'pip install --upgrade pip'
	            sh 'make deps'
	            sh 'make test'
        	}
        }
    }
}