pipeline {
    agent any

    stages {
        stage('Install Python3') {
            steps {
                sh 'sudo apt-get update'
                sh 'sudo apt-get install python3'
            }
        }
        stage('Run python file') {
            steps {
                sh 'python3 math.py'
            }
        }
    }
}
