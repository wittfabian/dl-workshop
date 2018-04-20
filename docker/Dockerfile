FROM continuumio/anaconda3
MAINTAINER "Fabian Witt"

# for proxy usage
# ENV http_proxy=
# ENV https_proxy=

RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN ["mkdir", "notebooks"]

ADD environment.yml environment.yml

RUN ["conda", "env", "create"]

COPY conf/.jupyter /root/.jupyter
COPY run_jupyter.sh /

RUN ["chmod", "+x", "/run_jupyter.sh"]

# Jupyter and Tensorboard ports
EXPOSE 8888 6006

# Store notebooks in this mounted directory
VOLUME /notebooks

CMD ["/run_jupyter.sh"]

# for proxy usage
# ENV http_proxy ""
# ENV https_proxy ""
