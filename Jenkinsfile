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
                    dir('jenkins-pipeline-test') { // Assuming 'jenkins-pipeline-test' is your project folder
                        sh 'ls'
                        sh 'source venv/Scripts/activate'
                        sh 'pip install -r requirements.txt'
                        sh 'python manage.py migrate'
                        sh 'python manage.py runserver'
                    }
                }
            }
        }
    }
}