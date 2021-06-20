pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
	            sh 'make deps'
        	}
        }
        stage('Tests') {
            steps {
	            sh 'make test'
        	}
        }
    }
}