pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing project dependencies'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                bat 'python -m pytest -v'
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