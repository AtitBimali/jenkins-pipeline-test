pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Build your Django application
                sh 'python manage.py collectstatic'
                sh 'python manage.py migrate'
            }
        }

        stage('Test') {
            steps {
                // Run tests for your Django application
                sh 'python manage.py test'
            }
        }

        stage('Deploy') {
            steps {
                // Deploy your Django application (using Ansible, for example)
                sh './deploy-script.sh'
            }
        }
    }
}
