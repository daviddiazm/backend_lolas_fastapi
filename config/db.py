import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

database_driver = os.getenv('DATABASE_DRIVER')
database_username = os.getenv('DATABASE_USERNAME')
database_password = os.getenv('DATABASE_PASSWORD')
database_host = os.getenv('DATABASE_HOST')
database_port = os.getenv('DATABASE_PORT')
database_name = os.getenv('DATABASE_NAME')

url = URL.create(
    drivername=database_driver,
    username=database_username,
    password=database_password,
    host=database_host,
    port=database_port,
    database=database_name
    
)

# url = URL.create(
#     drivername="mysql+pymysql",
#     username="root",
#     password="",
#     host="localhost",
#     port=3306,
#     database="lolas_db",
# )

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
