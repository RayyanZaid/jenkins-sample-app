pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                echo 'Building the project...'
                // Add any necessary build steps here (e.g., installing dependencies)
            }
        }
      
        stage('Unit Test') {
            steps {
                echo 'Running unit tests...'
                bat 'python -m unittest discover -s tests -p "test_*.py"'
            }
        }
    }
    
    post {
        
        
        success {
            echo 'All tests passed!'

            bat 'git config --global user.email "rayyanzaid0401@gmail.com"'
            bat 'git config --global user.name "RayyanZaid"'
            bat 'git checkout master'
            bat 'git merge --no-ff %BRANCH_NAME%'
            bat 'git push origin master'
        }
        
        failure {
            echo 'Some tests failed. Check the test reports for details.'
            // Additional actions to perform on failure
        }

    }
}
