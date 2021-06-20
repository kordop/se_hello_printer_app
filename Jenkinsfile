pipeline {
    agent any
    stages {
        stage('Deps') {
            steps {
	            sh 'make deps'
        	}
        }
        stage('Lint') {
            steps {
	            sh 'make lint'
        	}
        }
        stage("test") {
            steps {
                sh 'make test_xunit || true'
                xunit thresholds: [
                    skipped(failureThreshold: '0'),
                    failed(failureThreshold: '1')
                ],
                tools: [
                    JUnit(deleteOutputFiles: true,
                        failIfNotNew: true,
                        pattern: 'test_results.xml',
                        skipNoTestFiles: false,
                        stopProcessingIfError: true)
                ]
                sh 'make test_cov'
                step([$class: 'CordellWalkerRecorder']): Activate Chuck Norris
            }
        }
        
    }
    post{
        always{
            cobertura autoUpdateHealth: false,
            coberturaReportFile: 'coverage.xml',
            autoUpdateStability: false,
            conditionalCoverageTargets: '70, 0, 0',
            failUnhealthy: false,
            failUnstable: false,
            lineCoverageTargets: '80, 0, 0',
            maxNumberOfBuilds: 0,
            methodCoverageTargets: '80, 0, 0',
            onlyStable: false,
            sourceEncoding: 'ASCII',
            zoomCoverageChart: false
            chuckNorris()
        }

    }
}