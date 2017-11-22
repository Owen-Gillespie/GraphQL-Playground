# flask_sqlalchemy/schema.py
import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import SchoolClass as SchoolClassModel, Professor as ProfessorModel


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
schema = graphene.Schema(query=Query)
