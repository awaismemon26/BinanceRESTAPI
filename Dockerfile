FROM python:3.8.0-slim

# Setting PYTHONUNBUFFERED to 1 allows log messages to be dumped to the stream instead of being buffered.
ENV PYTHONUNBUFFERED 1

# Create directory and set it as working directory
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apt-get update \
&& apt-get install gcc -y \     
&& apt-get clean

RUN pip install -r requirements.txt

# CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "app:app"]