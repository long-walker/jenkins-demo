pipeline {
    agent any

    stages {
        stage('Welcome') {
            steps {
                echo 'Starting our modern scripted pipeline...'
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }
    }
}
