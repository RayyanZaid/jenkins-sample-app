pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Run main.py') {
            steps {
                bat "python main.py"
            }
        }
    }
}