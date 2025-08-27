# jenkins

### Setup Steps Performed:
1. Copied the Dockerfile from the [documentation](https://www.jenkins.io/doc/book/installing/docker/).
2. Ran the following commands:
```
docker build -t myjenkins-blueocean:2.516.2-1 .
```
```
docker run --name jenkins-blueocean --restart=on-failure --detach --network jenkins --env DOCKER_HOST=tcp://docker:2376 --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 --volume jenkins-data:/var/jenkins_home --volume jenkins-docker-certs:/certs/client:ro --publish 8080:8080 --publish 5000:5000 myjenkins-blueocean:2.516.2-1
```
3. Retrieved the password with this command:
```
docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword
```
4. Went to `localhost:8080` and signed in using the retrieved password
5. Downloaded recommended plugins
6. Created admin user
7. Restart (refresh the page)
8. Login with the new admin user

To connect into the master:
```
docker exec -it jenkins-blueocean bash
```
### Configuring Docker Cloud Agent
1. Install necessary plugins (Plugins -> Available plugins -> Search up Cloud Providers -> Check Docker -> Install)
2. Create a New Cloud (Manage Jenkins -> Clouds -> New Cloud)
- Cloud name - `docker`
- Type - `Docker`
3. Run the following set of commands:
```
docker run -d --restart=always -p 127.0.0.1:2376:2375 --network jenkins -v /var/run/docker.sock:/var/run/docker.sock alpine/socat tcp-listen:2375,fork,reuseaddr unix-connect:/var/run/docker.sock
```
```
docker inspect <container_id> | grep IPAddress
```
Copy the resulting IPAddress after running the commands.  Replace container_id with the created container (i.e 272add98c06899b0606476a51fe34b0f94b821f250488bfda65071a6ca7299da)
4. Add the following configurations:
- Docker Host URI - `tcp://<IPAddress>:2375`
- Enabled - ✅
- Inside Docker Agent Template:
    - Labels: `docker-agent-alpine`
    - Enabled: ✅
    - Name: `docker-agent-alpine`
    - Docker Image: `jenkins/agent:latest-jdk17`
    - Instance Capacity: `2`
Click Save once done.
5. Go back to your project you were working on and click `Configure`
6. Click on the `Restrict where this project can be run` and enter `docker-agent-alpine` as the `Label Expression`
7. Click save and run a build.

### Configure Jenkins Pipeline
Components of a Groovy Script
- Wrapped in pipeline {} block
- Add an agent {} block to indicate what node we will be using
- Next block is stages {} which would then generate each stage {} of the process
**NOTE:** If one stage fails, it does NOT continue with following stages
Template:
```
pipeline {
    agent {
        node {
            label 'jenkins-agent-goes-here'
            }
      }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                echo "doing build stuff.."
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff..
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}
```
Using a Jenkins file:

### NOTES:
- Data is found at `/var/jenkins_home`
- Workspace is found at `/var/jenkins_home/workspace`
    - The workspace is essentially where all the created files are stored when running through builds
    - Enable the `Delete workspace before build starts` to have new workspaces created per build
- Use the `BUILD_ID` environment variable to display the Build's run number
- Use the `BUILD_URL` environment variable to provide a direct link to the Build
- We can use Jenkins "Cloud" plugins to connect to remote machines
- Poll SCM is a Build Trigger than can help schedule when a build is run
Syntax - MINUTE HOUR DOM MONTH DOW
EX:      H/5    *     *   *    *
