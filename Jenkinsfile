pipeline {
    agent any
    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Run main.py') {
            when {
                branch "fix-*"
            }
            steps {
                bat "python main.py"
            }
        }
    }
}
