pipeline {
    agent any

    environment {
        DOCKER_BIN = '/usr/local/bin/docker'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set Up Python') {
            steps {
                sh 'python3 -m venv .venv'
                sh '.venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '.venv/bin/pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '${DOCKER_BIN} build -t aceest-fitness-app .'
            }
        }
    }
}
