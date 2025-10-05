pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/SOUNDARYAS45/jenkinpipline.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Build step...'
                sh 'python3 -m py_compile hello.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python3 -m unittest test_hello.py'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'hello.py', fingerprint: true
            }
        }
    }

    post {
        success { echo 'Pipeline completed successfully!' }
        failure { echo 'Pipeline failed!' }
    }
}
