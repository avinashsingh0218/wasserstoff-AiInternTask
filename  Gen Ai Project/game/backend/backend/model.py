from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GlobalGuessCount(Base):
    __tablename__ = "global_guesses"

    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True)
    count = Column(Integer, default=1)
