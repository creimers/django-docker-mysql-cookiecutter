FROM python:3.5

ADD . /project
WORKDIR /project

RUN mkdir -p /var/log/supervisor

RUN pip install --upgrade pip
RUN pip install -r requirements.txt


###############################################################################
#   service configuration    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#ADD ./etc/nginx.conf /etc/nginx/nginx.conf
#ADD ./etc/supervisor.conf /etc/supervisor/supervisor.conf
#ADD ./etc/uwsgi.ini /etc/cloudmesh/uwsgi.ini


#RUN python source/manage.py collectstatic --noinput

EXPOSE 80

CMD ["./service/env/bin/supervisord", "-c", "/etc/supervisor/supervisor.conf"]

CMD uwsgi etc/uwsgi.ini
