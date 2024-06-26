FROM python:3.10.14-alpine3.20

WORKDIR /app

RUN pip install sqlalchemy

RUN pip install psycopg2-binary

RUN pip install flask

COPY . .

EXPOSE 8001

CMD ["python", "App.py"]