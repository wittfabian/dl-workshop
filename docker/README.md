# Workshop Docker Container

We're building this container on top of [Debian 8 Docker container](https://hub.docker.com/r/library/debian/) and [Anaconda Docker container](https://hub.docker.com/r/continuumio/anaconda3/)

Build Docker container:
```sh
docker build . -f <path/to/Dockerfile> -t dl_workshop_container
```

Run Docker container:
```sh
docker run -it -p 8888:8888 -p 6006:6006 -d -v <path/to/dl-workshop/workshop>:/workshop dl_workshop_container
```

We're using following parameters:
- ```-p 8888:8888``` to export Jupyter Web interface
- ```-p 6006:6006``` to export TensorflowDashboard Web interface
- ```-d``` to run Docker container in background
- ```-v workshop:/workshop``` to mount *workshop* folder inside Docker container