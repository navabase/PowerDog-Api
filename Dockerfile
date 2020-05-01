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
EXPOSE $PORT
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.

CMD cd app && exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app