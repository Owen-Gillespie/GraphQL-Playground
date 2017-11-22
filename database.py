from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import date, time
import json

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from models import Professor, SchoolClass
    # Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    # Check for any courses in database
    # TODO: Figure out the clean way to check if the database is empty
    count = 0
    check = db_session.query(SchoolClass)
    for course in check:
        count += 1

    if count != 0:
        return

    print("initializing database from 'data.json'")
    try:
        course_data = json.load(open('data.json'))
    except IOError:
        print("put the initial course data into data.json")
    
    courses = course_data['courses']
    for course in courses:
        prof_names = course['faculty']
        # Todo: Handle multiple teachers well
        prof_name = prof_names[0]
        prof = Professor.query.filter_by(name=prof_name).first()
        if prof is None:
            prof = Professor(name=prof_name)
            db_session.add(prof)
        if course['schedule'] != []:
            start_time = course['schedule'][0]['startTime']
            end_time = course['schedule'][0]['endTime'] 
            days = course['schedule'][0]['days']
            if days == []:
                days = ""
        else:
            start_time = None
            end_time = None
            days = None
        course = SchoolClass(department=course['department'], number=course['courseNumber'], suffix=course['courseCodeSuffix'], school=course['school'], section=course['section'], name=course['courseName'],
                             professor=prof, open_seats = course['openSeats'], total_seats=course['totalSeats'], course_status=course['courseStatus'], days= days,
                             start_time= start_time, end_time=end_time, credits=course['quarterCredits'], start_date=course['startDate'],
                             end_date=course['endDate'])
        db_session.add(course)

    db_session.commit()

