FROM python:3.6

RUN mkdir -p /logs
RUN mkdir -p /app
WORKDIR /app
ENV TZ 'America/Sao_Paulo'
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD . /app
WORKDIR /app

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt


EXPOSE 8081

CMD ["/usr/local/bin/python","bots/app.py"]
#CMD gunicorn --bind 0.0.0.0:$PORT wsgi 