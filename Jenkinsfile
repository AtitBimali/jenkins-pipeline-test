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
                    dir('C:/Users/Atit Bimali/Documents/DevOps Learning/jenkins-pipeline-test') { // Assuming 'jenkins-pipeline-test' is your project folder
                        bat 'dir'
                        bat 'venv/Scripts/activate'
                        bat "\"C:/Users/Atit Bimali/AppData/Local/Programs/Python/Python311/Scripts/pip.exe\" install -r requirements.txt"
                        bat "\"C:/Users/Atit Bimali/AppData/Local/Programs/Python/Python311/Scripts/python.exe\" manage.py migrate"
                        bat "\"C:/Users/Atit Bimali/AppData/Local/Programs/Python/Python311/Scripts/python.exe\" manage.py runserver"
                    }
                }
            }
        }
    }
}