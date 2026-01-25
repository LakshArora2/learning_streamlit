# Container Image Creation for Loan Default Prediction Application
# This is a Dockerfile for a Flask application that predicts loan default using a pre-trained XGBoost model.
# these are set of instructions to build a docker image
# Image is a package that contains everything needed to run an application - code, runtime, libraries, environment variables, config files etc.
# We will build an image using the docker file and then run a container using that image.
# Base image - python + os - am telling the docker file to package python 3.10 slim version as the base image
FROM python:3.10-slim

# Creating a directory -create a directory/ folder inside the image called /app where our application code will reside
# this is a root level directory
WORKDIR /app

# Copying requirements file into the container directory
# All the libraries that our application depends on are listed in requirements.txt file
COPY requirements.txt .

# Installing the dependencies listed in requirements.txt file
# pip is package manager for python - it helps to install python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copying the application code and the pre-trained model into the container directory
# Only the application and model on which the application depends are copied into the container
COPY flask_app.py .
COPY xgb_loan_pred_model.pkl .
COPY target_encoder.pkl .

# Run the application on port 5000
EXPOSE 5000

# Using python to run the flask application
CMD ["python", "flask_app.py"]

# Run the command 'docker build -t loan-default-prediction-api .' to build the image

# Next code says that look at port 5000 in the container and map it to port 5000 on the host machine
# Run the command 'docker run -p 5000:5000 loan-default-prediction-api' to run the container

#  To share the docker image, first login to docker hub using 'docker login' command
# Then tag the image using 'docker tag loan-default-prediction-api lakshayarora333/loan-default-prediction-api:latest'
# Finally push the image to docker hub using 'docker push lakshayarora333/loan-default-prediction-api:latest'


# Search in google as "Python base image docker" for ready docker images with python installed