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
                dockerImage.inside {
                    // Set the working directory to the absolute path within the container
                    def containerWorkspace = "/workspace/${JOB_NAME}/${BUILD_NUMBER}"
                    sh "mkdir -p ${containerWorkspace}" // Create the directory if it doesn't exist
                    sh "python manage.py migrate"
                    sh "python manage.py runserver 0.0.0.0:8000"
                }
            }
        }
    }

    }
}
