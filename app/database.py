from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time 
import psycopg2
from psycopg2.extras import RealDictCursor
from .config import settings


# SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:Trumpet79?@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# create dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()


        
# keep trying to connect ot the database 
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost", 
#             database="fastapi", 
#             user="postgres", 
#             password="Trumpet79?", 
#             cursor_factory=RealDictCursor
#         )

#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break

#     except Exception as error:
#         print("Connecting to database failed :(")
#         print("Error: ", error)
#         time.sleep(2)
