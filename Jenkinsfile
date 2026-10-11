pipeline {
    agent {
        docker {
            image 'python:3.12-slim'
            args '-u root'
        }
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Build') {
            steps {
                sh 'python --version'
                sh 'python -m pip install --upgrade pip'
                sh 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Smart Parking CI Pipeline completed successfully!'
        }
        failure {
            echo 'Smart Parking CI Pipeline failed. Check the console output.'
        }
    }
}