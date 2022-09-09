FROM tiangolo/uwsgi-nginx-flask:python3.10
RUN pip install --upgrade pip
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
COPY ./requirements.txt /var/www/requirements.txt
RUN echo "uwsgi_read_timeout 300s;" > /etc/nginx/conf.d/custom_timeout.conf
RUN pip install -r /var/www/requirements.txt