// node{
    
//     stage('GitHub Checkout'){
//         git branch: 'master', credentialsId: 'git-creds', url: 'https://github.com/anishmoktan/devbops_user_microservice'
//     }
    
//     stage('DevBops User Test'){
//         sh 'python3 Test.py'
//     }
    
//     stage('Docker Image Build'){
//         sh 'docker build -t anishmoktan/devbops_user .'
    
//     }

//     stage('Docker Image Push'){

//         withCredentials([string(credentialsId: 'docker-pwd', variable: 'dockerHubPwd')]) {
//             sh "docker login -u anishmoktan -p ${dockerHubPwd}"
    
//             }
        
//         sh 'docker push anishmoktan/devbops_user'
    
//     }

//     stage('Run Docker conatiner on Private EC2'){
//         def dockerRm = 'docker rm -f devbops_user'
//         def dockerRmI = 'docker rmi anishmoktan/devbops_user'
//         def dockerRun = 'docker run -p 8090:80 -d --name devbops_user anishmoktan/devbops_user'
//         sshagent(['docker-server']) {
//             sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRm}"
//             sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRmI}"
//             sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.85 ${dockerRun}"
           
//         }
//     }   
    
// }

