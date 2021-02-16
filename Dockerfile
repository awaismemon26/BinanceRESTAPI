FROM python:3.8.0-slim

# Setting PYTHONUNBUFFERED to 1 allows log messages to be dumped to the stream instead of being buffered.
ENV PYTHONUNBUFFERED True

# Create directory and set it as working directory
# RUN mkdir /app
# WORKDIR /app
# COPY . /app

RUN apt-get update \
&& apt-get install gcc -y \     
&& apt-get clean

# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running pip install on every code change.
COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./



#CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "wsgi:app"]
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 wsgi:app