FROM java:8-jdk
WORKDIR /tmp
RUN wget http://archive.apache.org/dist/lucene/solr/6.5.1/solr-6.5.1.tgz
RUN tar xvfz solr-6.5.1.tgz
EXPOSE 8983
CMD /tmp/solr-6.5.1/bin/solr start -force -f
#The Linux dIstribution version used is Debain 8
