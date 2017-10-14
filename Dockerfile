FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

COPY ./app /app
