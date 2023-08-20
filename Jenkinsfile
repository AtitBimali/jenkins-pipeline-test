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
                script {
                    sh "python -m venv venv" // Create a virtual environment
                    sh "source venv/bin/activate" // Activate the virtual environment
                    
                    sh "pip install -r requirements.txt" // Install Django and other dependencies
                    
                    sh "python manage.py migrate"
                    sh "python manage.py runserver"
                }
            }
        }
