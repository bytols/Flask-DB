from sqlalchemy import create_engine
from sqlalchemy.engine import URL

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="admin123",
    host="localhost",
    port=5433,
    database="postgres"
)

engine = create_engine(url)

engine.connect()
