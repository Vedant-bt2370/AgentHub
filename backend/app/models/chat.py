from sqlalchemy import Column, Integer, String
from database.postgres import Base

class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)