FROM nginx:latest

RUN mkdir -p /app

COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./ /usr/share/nginx/html

WORKDIR /usr/share/nginx/html
