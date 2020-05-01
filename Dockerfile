# FROM node:11.13.0-alpine

# # create destination directory
# RUN mkdir -p /usr/src/api
# WORKDIR /usr/src/api

# # update and install dependency
# RUN apk update && apk upgrade
# RUN apk add python3
# RUN apk add git

# # copy the app, note .dockerignore
# COPY . /usr/src/api/
# RUN pip3 install --no-cache-dir -r requirements.txt
 

# # build necessary, even if no static files are needed,
# # since it builds the server as well


# # expose 5000 on container
# ENV PORT 8080
# EXPOSE $PORT

# # start the app

# CMD ["python3" ,"app/__main__.py"]
# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Install production dependencies.
RUN pip install Flask gunicorn

# Copy local code to the container image.
WORKDIR /api
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
# Service must listen to $PORT environment variable.
# This default value facilitates local development.
ENV PORT 8080

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
RUN cd app/

CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app