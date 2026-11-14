pipeline {
    agent any
    environment {
        IMAGE = "sandeep262005/flask-app:${BUILD_NUMBER}"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build Docker Image') {
            steps { sh 'docker build -t $IMAGE .' }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                        usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $IMAGE'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'sed -i "s|IMAGE_PLACEHOLDER|$IMAGE|g" k8s/deployment.yaml'
                sh 'kubectl apply -f k8s/deployment.yaml'
                sh 'kubectl rollout status deployment/flask-app'
            }
        }
    }
    post {
        success { echo "Deployed! Open http://23.22.76.155:30080" }
    }
}
