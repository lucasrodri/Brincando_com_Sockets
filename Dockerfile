FROM httpd:2.4

COPY ./html2/ /usr/local/apache2/htdocs/
RUN rm -rf /usr/local/apache2/htdocs/index.html