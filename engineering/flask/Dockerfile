###################################################################
# Build image:                                                    #
#   docker build --tag="flask-engineering" .                      #
#                                                                 #
# Run container:                                                  #
#   docker run -d -p 80:80 flask-engineering                      #
###################################################################
FROM alpine:3.4

# Update
RUN apk add --update \
    python py-mysqldb py-pip \
    && rm -rf /var/cache/apk/*

# Install app dependencies
RUN pip install Flask flask_restful Flask-MySQL

# Bundle app source
COPY app.py /src/app.py

EXPOSE 80 5000
CMD ["python", "/src/app.py", "-p 80"]
