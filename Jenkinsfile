pipeline {
    agent any
    
    environment {
        WORKSPACE_DIR = "/var/jenkins/workspace/${JOB_NAME}" // Using an environment variable for the workspace path
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Deploy') {
            steps {
                script {
                    def dockerImage = docker.build("my-django-app")
                    
                    // Using the environment variable for the working directory in the Docker container
                    dockerImage.inside("-w ${env.WORKSPACE_DIR}") {
                        sh "python manage.py migrate"
                        sh "python manage.py runserver 0.0.0.0:8000"
                    }
                }
            }
        }
    }
}
