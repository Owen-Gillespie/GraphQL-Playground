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
        return CreateProfessor(professor = new_prof)

class Mutation(graphene.ObjectType):
    create_professor = CreateProfessor.Field()    

schema = graphene.Schema(query=Query, mutation=Mutation)
