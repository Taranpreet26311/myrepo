FROM ubuntu:18.04
RUN apt-get update -y
RUN apt install nginx -y
RUN mkdir sites
RUN cd sites
RUN mkdir demo
COPY demo /root/sites/demo
RUN cd /root/sites
RUN cp demo /sites
COPY nginx.conf /etc/nginx/
RUN service nginx restart
CMD ["nginx", "-g", "daemon off;"]
