from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

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
    print(engine)
    print(Base.metadata)
    gerbode = Professor(name='Sharon Gerbode')
    db_session.add(gerbode)
    dodds = Professor(name = 'Zach Dodds')
    db_session.add(dodds)

    # cs5 = SchoolClass(name = 'Intro to CS', professor = dodds, days = "MWF", credits = 3, course_status = "Closed")
    # db_session.add(cs5)
    db_session.commit()

