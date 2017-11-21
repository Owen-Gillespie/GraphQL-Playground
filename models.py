from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Professor(Base):
    __tablename__ = 'professor'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class SchoolClass(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    days = Column(String)
    start_time = Column(String)
    end_time = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    credits = Column(Float)
    professor_id = Column(Integer,ForeignKey('professor.id'))
    professor = relationship(Professor, backref=backref('classes', uselist=True, cascade='delete,all'))
    open_seats = Column(Integer)
    total_seats = Column(Integer)
    course_status = Column(String)


