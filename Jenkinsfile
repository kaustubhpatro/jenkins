pipeline {
    agent any

    stages {
        stage('Install Python3') {
            steps {
                sh apt-get update
                sh apt-get install python3
            }
        }
        stage('Run python file') {
            steps {
                sh 'python3 math.py'
            }
        }
    }
}
