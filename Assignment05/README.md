## Deploy ToDo API[^2] on <a href="https://console.liara.ir">Liara</a> by Docker
- In this assignment, I deploy my FastAPI project from assignment 4 by writing a Dockerfile.

### Docker commands:[^1]
| Command | Description |
| --- | --- |
| docker images | show all images | 
| docker ps -a | show all containers | 
| docker build -t \<image name> . | build docker image with preferred name | 
| docker run -d -p 80:80 \<image name> | running docker container based on specific image on port 80|
| docker stop \<container ID or name> | stop container by specific name or id | 
| docker rm \<container ID or name> | remove container by specific name or id | 
| docker image rm \<image ID or name> | remove specific image | 


[^2]: <a href='https://github.com/BenyaminZojaji/PyDeploy-Course/tree/main/Assignment04/todoApp_API'>Assignment 4</a>
[^1]: I am writing these commands because this is a tutorial repository.
