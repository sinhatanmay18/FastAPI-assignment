from sqlalchemy import Column, Integer, String, Float
from database import Base


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    request_body = Column(String(20000))
    response_body = Column(String(250))
    processing_time = Column(Float)
