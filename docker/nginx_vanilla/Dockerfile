FROM ubuntu:18.04
RUN apt-get update -y
RUN apt install nginx -y
RUN service nginx restart
EXPOSE 80
EXPOSE 5555
EXPOSE 12233
CMD ["nginx", "-g", "daemon off;"]
