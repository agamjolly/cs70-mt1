FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./src /app
EXPOSE 80