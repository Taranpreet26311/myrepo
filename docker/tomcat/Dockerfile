FROM ubuntu:latest
RUN apt-get update -y
RUN apt install default-jdk
RUN apt install wget
RUN wget https://www-eu.apache.org/dist/tomcat/tomcat-9/v9.0.30/bin/apache-tomcat-9.0.30.tar.gz
RUN tar xf /tmp/apache-tomcat-9.0.30.tar.gz -C /opt/tomcat
