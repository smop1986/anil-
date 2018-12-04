pipeline {

    agent any
    
    stages {

       stage('Clear Workspace') {
            steps {
                echo 'Clear Workspace'
                deleteDir()
            }
        }

        stage('Checkout') {
            steps {
                echo 'Checkout'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build'
                sh "PYTHONSSLVERIFY=0 JIRA_SERVER=https://jira.com/rest/api/2/issue/key JIRA_USER=user JIRA_PASSWORD=password APP_PORT=5001 python flask_app.py"
               
            }
        }

    }
}
