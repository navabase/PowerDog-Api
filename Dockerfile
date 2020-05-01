FROM node:11.13.0-alpine

# create destination directory
RUN mkdir -p /usr/src/api
WORKDIR /usr/src/api

# update and install dependency
RUN apk update && apk upgrade
RUN apk add python3
RUN apk add git

# copy the app, note .dockerignore
COPY . /usr/src/api/
RUN pip3 install --no-cache-dir -r requirements.txt
 

# build necessary, even if no static files are needed,
# since it builds the server as well


# expose 5000 on container
EXPOSE $PORT

# start the app
ENTRYPOINT [ "app" ]
CMD ["python3" ,"__main__.py"]
