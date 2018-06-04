FROM ubuntu

# System requirements
RUN apt-get update && apt-get install -y \
  build-essential \
  curl \
  python3-pip \
  swig \
  libfreetype6-dev \
  libsdl-dev \
  libsdl-image1.2-dev \
  libsdl-ttf2.0-dev \
  libsmpeg-dev \
  libportmidi-dev \
  libavformat-dev \
  libsdl-mixer1.2-dev \
  libswscale-dev \
  supervisor \
  nodejs \
  npm \
  vim \
  nginx \
  libjpeg-dev && rm -rf /var/lib/apt/lists/*


# Upgrade pip then install dependencies
RUN pip3 install --upgrade pip

# Install
RUN pip3 install \
    gunicorn \
    Flask

RUN /usr/bin/npm install -g \
    ionic

RUN rm /etc/nginx/sites-enabled/default

COPY conf/nginx/monstergen.conf /etc/nginx/sites-enabled/
RUN ln -s /etc/nginx/sites-enabled/monstergen.conf /etc/nginx/sites-available/monstergen

COPY conf/supervisord/ /etc/supervisor/

COPY scripts/ /docker
RUN chmod u+x /docker/entrypoint.sh

EXPOSE 5000
WORKDIR /monstergen
CMD ["/docker/entrypoint.sh"]