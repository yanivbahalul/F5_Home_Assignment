FROM ubuntu:24.04

#install nginx
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/*

#remove defualt config
RUN rm /etc/nginx/sites-enabled/default

#copy custom config
COPY servers.conf /etc/nginx/sites-enabled/servers.conf

#copy html files
COPY src/html/index.html /var/www/html/index.html

#expose ports
EXPOSE 8080 8000

#start nginx
CMD ["nginx", "-g", "daemon off;"]
