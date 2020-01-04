# Create a docker container for the steel plate fault prediction service
1. Create the container using the following command
```
$ docker build . -t cs6220/final_project
```
2. Run the container using following command
```
$ docker run -d -p 8080:8080 --name steel-plate-fault-classifier cs6220/final_project:latest
```
3. Start the server using command
```
$ docker run cs6220/final_project
```
4. Go to http://0.0.0.0:8080/ to make prediction

Note:
1. use '$ docker ps' to check the container that are running
2. use '$ docker stop CONTAINER_ID' to stop a running container

