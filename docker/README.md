# Installation via Docker

We're building this container on top of [Debian 8 Docker container](https://hub.docker.com/r/library/debian/) and [Anaconda Docker container](https://hub.docker.com/r/continuumio/anaconda3/)

Build Docker container:
```sh
docker build . -f <absolute/path/to/Dockerfile> -t dl_workshop_container
```


Run Docker container:
```sh
docker run -it -p 8888:8888 -p 6006:6006 -d -v <absolute/path/to/dl-workshop/notebooks>:/notebooks dl_workshop_container
```


We're using the following parameters:
- ```-p 8888:8888``` to export Jupyter Web interface
- ```-p 6006:6006``` to export Tensorboard Web interface
- ```-d``` to run Docker container in background
- ```-v notebooks:/notebooks``` to mount *notebooks* folder inside Docker container


The notebooks are available under the following url:
```sh
http://localhost:8888
```

