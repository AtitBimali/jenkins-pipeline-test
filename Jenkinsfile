pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                // Build steps (e.g., collect static files, compile assets)
            }
        }
        
        stage('Test') {
            steps {
                // Testing steps (e.g., run unit tests)
            }
        }
        
        stage('Deploy') {
            steps {
                // Deploy the Django application using Docker
                script {
                    def dockerImage = docker.build("my-django-app")
                    
                    dockerImage.inside {
                        sh "python manage.py migrate" // Apply migrations
                        sh "python manage.py runserver 0.0.0.0:8000" // Run Django server
                    }
                }
            }
        }
    }
}
