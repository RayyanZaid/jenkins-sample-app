pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }

        stage('cat README') {
            when {
                branch "fix-*"
            }

            stage('Display README') {
            steps {
                // Display the contents of README.md (for Windows)
                bat 'type README.md'
            }
        }
        }
    }
}