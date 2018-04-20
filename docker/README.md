# Installation via Docker

We're building this container on top of [Debian 8 Docker container](https://hub.docker.com/r/library/debian/) and [Anaconda Docker container](https://hub.docker.com/r/continuumio/anaconda3/).

## Installation of Docker Daemon
Download and install the Docker Daemon from the [Docker Website](https://www.docker.com/) for your OS.

### Proxy Configuration in the Docker Daemon
Docker will download all the necessary files for the build process from the internet so it might be necessary to configure a proxy. You can switch to a manual proxy configuration in the Docker Daemon Settings under Proxies.

## Build Docker Container
Now you need to build the docker container. Navigate in the terminal into the repository directory and then into the docker directory ```dlworkshop/docker```.

### Proxy Configuration in the Dockerfile
In case you need a proxy and you have set it correctly in the Docker Daemon, you need to set it in the Docker file as well. Uncomment the four corresponding lines under the ```# for proxy usage``` headlines and add your proxy in the first two lines. The last two lines remain empty so there is no need for a change.

### Execute the Build Command
Now execute in the ```dlworkshop/docker``` directory the following command.

```sh
docker build . -f Dockerfile -t dl_workshop_container
```

## Run Docker Container
After the build process was successfully done you can run the container.

```sh
docker run -it -p 8888:8888 -p 6006:6006 -d -v <absolute/path/to>/dlworkshop/notebooks:/notebooks dl_workshop_container
```

We're using the following parameters:
- ```-p 8888:8888``` to export Jupyter Web interface
- ```-p 6006:6006``` to export Tensorboard Web interface
- ```-d``` to run Docker container in background
- ```-v notebooks:/notebooks``` to mount *notebooks* folder inside Docker container

## Accessing and Running the Notebooks
The notebooks are now available in your browser under the following url:

```sh
http://localhost:8888
```

