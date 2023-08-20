pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out the code from the repository
                checkout scm
            }
        }

        // stage('Build') {
        //     steps {
        //         // Build your Django application
        //         // sh 'python manage.py collectstatic'
        //         // sh 'python manage.py migrate'
        //     }
        // }

        // stage('Test') {
        //     steps {
        //         // Run tests for your Django application
        //         sh 'python manage.py test'
        //     }
        // }

        stage('Deploy') {
            steps {
                script {
                    dir('C:/Users/Atit Bimali/Documents/DevOps Learning/jenkins-pipeline-test') {
                        sh 'ls'
                        sh 'source venv/Scripts/activate' // Activate the virtual environment
                        sh 'pip install -r requirements.txt' // Install dependencies
                        sh 'python manage.py migrate' // Apply migrations
                        sh 'python manage.py runserver' // Run Django server
                    }
                }
            }
        }
    }
}