node {
   def app
 
   stage('GitHub Checkout') {
       checkout scm
   }
 
   stage('Docker Build') {
 
       app = docker.build("anishmoktan/devbops_user_v")
   }
 
   stage('Python Test in Container') {
      
       app.inside {
           sh 'python3 Test.py'
       }
   }
 
   stage('Docker Image Push') {
       docker.withRegistry('https://registry.hub.docker.com', 'docker-hub') {
           app.push("${env.BUILD_NUMBER}")
           }
   }
 
   stage('Run Docker Containers in Private EC2'){
       // def priorV = (env.BUILD_NUMBER - 1)
       def dockerRm = 'docker rm -f devbops_user'
       def dockerPrune = 'docker image prune -a -f'
       // def dockerRmI = "docker rmi anishmoktan/devbops_user_v:${priorV}"
       def dockerRun = "docker run -p 8090:80 -d --name devbops_user anishmoktan/devbops_user_v:${env.BUILD_NUMBER}"
       sshagent(['docker-server']) {
           // sh "echo ${env.BUILD_NUMBER - 1}"
           sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRm}"
           sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerPrune}"
           // sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRmI}"
           sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRun}"
       }
   }
}
