from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Time, Enum
from sqlalchemy.orm import relationship, backref
from database import Base
from enum import Enum

# TODO: Make Course status an enum
# TODO: Look into making school an emum


class Professor(Base):
    __tablename__ = 'professor'
    id = Column(Integer, primary_key=True)
    name = Column(String)

class SchoolClass(Base):
    __tablename__ = 'schoolclass'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Course code info
    department = Column(String)
    number = Column(Integer)
    suffix = Column(String)
    school = Column(String)
    section = Column(String)

    days = Column(String)

    #start_time = Column(Time)
    start_time = Column(String)

    #end_time = Column(Time)
    end_time = Column(String)

    #start_date = Column(Date)
    start_date = Column(String)

    #end_date = Column(Date)
    end_date = Column(String)

    credits = Column(Float)
    professor_id = Column(Integer,ForeignKey('professor.id'))
    professor = relationship(Professor, backref=backref('classes', uselist=True, cascade='delete,all'))
    open_seats = Column(Integer)
    total_seats = Column(Integer)
    course_status = Column(String)
