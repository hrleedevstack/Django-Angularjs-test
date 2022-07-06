FROM python:3.8.10-slim-buster

WORKDIR /workspace
COPY . django-angular-test/

RUN python -m pip install --no-cache-dir --upgrade pip && python -m pip install -r /workspace/django-angular-test/requirement.txt
CMD ["python", "/workspace/django-angular-test/data_server/manage.py", "runserver", "0:5123"]