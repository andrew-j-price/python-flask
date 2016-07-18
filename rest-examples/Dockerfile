###################################################################
# Build image:                                                    #
#   docker build --tag="flask-rest-examples" .                    #
#                                                                 #
# Run container:                                                  #
#   docker run -d -p 80:80 flask-rest-examples                    #
###################################################################
FROM alpine:3.4

# Update
RUN apk add --update python py-pip && \
    rm -rf /var/cache/apk/*

# Install app dependencies
RUN pip install Flask

# Bundle app source
COPY app.py /src/app.py

EXPOSE 80
CMD ["python", "/src/app.py", "-p 80"]
