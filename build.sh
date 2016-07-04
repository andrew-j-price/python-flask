# Build the images
docker build --tag="flask-app" ./simple-app/
docker build --tag="flask-rest" ./simple-rest/
docker build --tag="gamut-basic" ./gamut-basic/
