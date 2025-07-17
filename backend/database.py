from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ⚠️ Reemplazá con tus propios datos si cambian
DATABASE_URL = "mysql+mysqlconnector://root:LupeSecure_2025@localhost:3306/infomundi"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
