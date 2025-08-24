# jenkins

Setup Steps Performed:
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

NOTES:
- Data is found at `/var/jenkins_home`
- Workspace is found at `/var/jenkins_home/workspace`
    - The workspace is essentially where all the created files are stored when running through builds
    - Enable the `Delete workspace before build starts` to have new workspaces created per build
- Use the `BUILD_ID` environment variable to display the Build's run number
- Use the `BUILD_URL` environment variable to provide a direct link to the Build