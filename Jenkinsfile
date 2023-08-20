pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Create Docker Image') {
            steps {
                script {
                    dir('C:/Users/Atit Bimali/Documents/DevOps Learning/jenkins-pipeline-test') {
                        // Build your Django application
                        bat 'venv/Scripts/activate'
                        bat "\"C:/Users/Atit Bimali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe\" install -r requirements.txt"
                        bat "\"C:/Users/Atit Bimali/AppData/Local/Programs/Python/Python311/python.exe\" manage.py migrate"
                        // Build Docker image using the existing Dockerfile
                        bat 'docker build -t my-django-app -f Dockerfile .'
                    }
                }
            }
        }

        stage('Deploy with Docker') {
            steps {
                script {
                    // Run the Docker container
                    bat 'docker run -d -p 8000:8000 --name your-django-container your-django-image'
                }
            }
        }
    }
}
