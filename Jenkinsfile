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

        stage('Deploy to Production') {
            steps {
                echo '🚀 Deploying code to the production server...'
                echo '✅ Deployment complete! App is live.'
            }
        }
    }
}
