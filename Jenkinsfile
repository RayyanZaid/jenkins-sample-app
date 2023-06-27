pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Prepare the workspace
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                // Run unit tests
                sh 'python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy the application (example: copy files to a server)
                sh 'python deploy.py'
            }
        }
    }
}
