FROM python:3.8

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt

COPY dnd/ /app

WORKDIR /app

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["python3", "manage.py", "runserver", "0:8000"]
