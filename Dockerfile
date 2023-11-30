FROM python:3.10

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./sisinf /app

WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh","/entrypoint.sh" ]
