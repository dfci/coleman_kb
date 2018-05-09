FROM ubuntu:14.04
MAINTAINER Priti Kumari <priti@jimmy.harvard.edu>

# install required ubuntu packages
RUN DEBIAN_FRONTEND=noninteractive apt-get update --fix-missing && apt-get install -y \
    build-essential \
    unzip \
    pkg-config \
    python-dev \
    python-matplotlib \
    python-pip \
    libaio-dev \
    libssl-dev \
    libffi-dev \
    libfreetype6-dev \
    libpng-dev \
    nano \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/*

# copy over and install requirements
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# copy application to image
COPY ./colemankb /colemankb
COPY ./app.py /app.py

ENTRYPOINT ["python"]
CMD ["app.py"]

# enable nano debugging (i hate vi)
ENV TERM xterm