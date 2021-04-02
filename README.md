# Binance REST API Python

## Description
This application uses Flask micro web framework for creating REST API. The purpose of this API is to fetch account information from Binance and expose it using Account Endpoints for further operations.   

# Local Development Enviornment
- VS Code 
- Python 3.8.0
- Local built-in WSGI server
# Making REST ready to be served 
- **Gunicorn** it is one of many python WSGI server which is basically application web server that will be running behind nginx. It acts as a medium between server and Flask app.

- **NGINX** is a web server to server static files. It is front facing web server that will handle requests.

## Commands 

- **gunicorn --bind 0.0.0.0:8080 app:app** (Activating gunicorn to serve the project)

# Dockerizing Flask Application
Containarizing our application to make it portable and to ship, build and run with all our dependencies because everything needed for our app to run will be included.

## Commands
- **Docker run -d --rm -p 8080:8080 --name binancerestapi binancerestapi:v1** (to run docker container)

# Deploying our Container to Cloud
After we have tested our docker containers on local enviornment, now it's time to deploy our containers on cloud. **I will be choosing Google Cloud Run Serverless Platform**
which is fully managed serverless platform to deploy scalable containerized application.

## Commands for deployment
To deploy our image to Google, we will use the following command to build an image on Google Builds
- **gcloud builds submit --tag gcr.io/binance-rest-api/binancerestapi:v1**

After successfull build, our image will be hosted on Container Registery section.

To run our docker container: 

-**gcloud run deploy binancerestapi --image gcr.io/binance-rest-api/binanceresapi:v1**


URL 

[https://binancerestapi-cghrvekmwa-uc.a.run.app/api/v1/accounts](https://binancerestapi-cghrvekmwa-uc.a.run.app/api/v1/accounts)