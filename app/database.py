from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
                                      #<usernam>:<password>@<hostname>/<database name>
#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DB_USERNAME}:112517@localhost:5432/fastapi"
#SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Reference for raw SQL database connection via psycopg lib
#
# while True:
#    try:
#       conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="112517", cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print('database connection succesfull')
#        break
#    except Exception as error:
#        print("db connect failled")
#        print("Error: ", error)
#        time.sleep(2)