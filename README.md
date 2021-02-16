# Binance REST API Python API 
This API uses Flask micro web framework. 

# Deployement 
Gunicorn is a Python WSGI server that runs Python web application code. Gunicorn is one of many WSGI server implementations

The following command is for activating gunicorn to serve the project
**gunicorn --bind 0.0.0.0:5000 app:app** 
Now, you can test API running

# To run Docker image 
**Docker run -d --rm -p 5000:5000 --name binancerestapi binancerestapi:v1**

## Libraries Required
All libraries required by the project is mentioned inside requirement.txt file