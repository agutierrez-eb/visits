FROM python:alpine

WORKDIR usr/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY ./ ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# http://github.com/andymccurdy/redis-py