FROM ubuntu:24.04

#install nginx
RUN apt-get update && apt-get install -y \
    nginx \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

#copy custom config
COPY servers.conf /etc/nginx/sites-enabled/servers.conf

#copy html files
COPY src/html/ /var/www/html/

#expose ports
EXPOSE 8080 8000

#start nginx
CMD ["nginx", "-g", "daemon off;"]
