FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.python.org -r /app/requirements.txt

CMD ["bash", "start.sh"]