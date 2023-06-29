pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                // You can add any necessary build steps here (e.g., installing dependencies)
            }
        }
        
        stage('Unit Test') {
            steps {
                echo 'Running unit tests...'
                sh 'python -m unittest discover -s tests -p "test_*.py"'
            }
        }
    }
    
    post {
        always {
            junit 'tests/**/TEST-*.xml'
        }
        
        success {
            echo 'All tests passed!'
            // Additional actions to perform on success
        }
        
        failure {
            echo 'Some tests failed. Check the test reports for details.'
            // Additional actions to perform on failure
        }
    }
}
