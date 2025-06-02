from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    gitlab_username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    role = Column(String)  # 'ai-dev', 'tech-lead', 'admin'

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    topic = Column(String)
    date = Column(DateTime, default=datetime.utcnow)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    session_id = Column(Integer, ForeignKey("sessions.id"))
    validated_by = Column(Integer, ForeignKey("users.id"))
    is_present = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
