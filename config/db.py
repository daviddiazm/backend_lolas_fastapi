from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="",
    host="localhost",
    port=3306,
    database="lolas_db",
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
