from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import date, time
engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import Professor, SchoolClass
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    # create fixtures
    gerbode = Professor(name='Sharon Gerbode')
    db_session.add(gerbode)
    dodds = Professor(name = 'Zach Dodds')
    db_session.add(dodds)

    cs5 = SchoolClass(name = 'Intro to CS', professor = dodds, days = "MWF", credits = 3, course_status = "Closed", start_date = date(2017, 8, 17), end_date = date(2017, 12, 15), start_time = time(9), end_time=time(9,50), department="CSCI", number=5, suffix="", school="HM", section=1)
    db_session.add(cs5)
    db_session.commit()

