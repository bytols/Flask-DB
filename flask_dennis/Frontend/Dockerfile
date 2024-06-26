FROM python:3.10.14-alpine3.20

WORKDIR /app

RUN pip install flask

RUN pip install requests

COPY . .

COPY ./templates ./templates

EXPOSE 8008

CMD ["python", "App.py"]