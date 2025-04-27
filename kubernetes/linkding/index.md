# Notes

These were the list of steps that I took to get linkding to work on my local machine
- I copied over the files used for mealie's deployment process `cp mealie/* linkding`
- I then modified each files yaml configuration where it said mealie to linkding
    - This was done by using vim and used the string substitution `:%s/mealie/linkding/g`
- Initially, I ran the `kubectl -f apply [file_name]` for the three files
- Each file's apply ran successfully
- When checking the service using `kubectl get svc -n linkding`, I noticed that the external-ip was set to pending
- This led me to realize that I had a port conflict with mealie through copying the same port (8000)
- I deleted the service for mealie and that resolved the external-ip issue
- The next issue I had was that the webpage was not appearing when going to localhost:8000
- Going through the [docker-compose.yml](https://github.com/sissbruecker/linkding/blob/master/docker-compose.yml) file, I found that the port needed was actually 9090
- After making this change for both the service.yml and deployment.yml files, the website was working!
- I had to create a superuser and to do that I did the following
    - `kubectl exec -it linkding-xxxxx-xxxxx -- /bin/bash`: Create a bash shell into the pod
    - python3 manage.py createsuperuser --username=joe --email=joe@example.com
    - Sign in with those credentials

After following all these steps, we saw the result of a fully functioning linkding!
