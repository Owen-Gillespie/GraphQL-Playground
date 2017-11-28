# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import SchoolClass as SchoolClassModel, Professor as ProfessorModel
from database import db_session

class SchoolClass(SQLAlchemyObjectType):
    class Meta:
        model = SchoolClassModel
        interfaces = (relay.Node, )


class Professor(SQLAlchemyObjectType):
    class Meta:
        model = ProfessorModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_classes = SQLAlchemyConnectionField(SchoolClass)
    all_professors = SQLAlchemyConnectionField(Professor)



class CreateProfessor(graphene.Mutation):

    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    professor = graphene.Field(Professor)

    def mutate(self, info, name):
        new_prof = ProfessorModel(name=name)
        db_session.add(new_prof)
        db_session.commit()
        ok = True
        return CreateProfessor(professor = new_prof, ok=ok)

class CreateSchoolClass(graphene.Mutation):

    class Arguments:
        name = graphene.String()
        department = graphene.String()
        number = graphene.Int()
        suffix = graphene.String()
        school = graphene.String()
        section = graphene.String()
        days = graphene.String()
        start_time = graphene.String()
        end_time = graphene.String()
        start_date = graphene.String()
        end_date = graphene.String()
        credits = graphene.Int()
        open_seats = graphene.Int()
        total_seats = graphene.Int()
        course_status = graphene.String()
        professor_name = graphene.String()

    ok = graphene.Boolean()
    school_class = graphene.Field(SchoolClass)

    def mutate(self, info, name, department, number, suffix, school, section, days,
               start_time, end_time, start_date, end_date, credits, open_seats,
               total_seats, course_status, professor_name):

        prof = ProfessorModel.query.filter_by(name=professor_name).first()
        if prof is None:
            prof = Professor(name=prof_name)
            db_session.add(prof)
        new_course = SchoolClassModel(department=department, number=number, suffix=suffix,
                                      school=school, section=section, name=name, professor=prof,
                                      open_seats=open_seats, total_seats=total_seats, days=days,
                                      start_time=start_time, end_time=end_time, credits=credits,
                                      start_date=start_date, end_date=end_date)
        db_session.add(new_course)
        db_session.commit()
        ok=True
        return CreateSchoolClass(school_class=new_course, ok=ok)

class Mutation(graphene.ObjectType):
    create_professor = CreateProfessor.Field()
    createSchoolClass = CreateSchoolClass.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
