FROM ubuntu:18.04
RUN apt-get update -y
RUN apt install nginx -y
COPY nginx.conf /etc/nginx/
RUN service nginx restart
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
