docker build -t app_backend .
# docker run localhost/app_backend:latest
docker run --rm -it --network=host localhost/app_backend:latest