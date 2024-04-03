import os
import graphene
from flask import Flask
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from flask_graphql import GraphQLView
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column, Integer, String

DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL, convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class PartModel(Base):
    __tablename__ = 'parts'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    compatible_with = Column(String)

class Part(SQLAlchemyObjectType):
    class Meta:
        model = PartModel
        interfaces = (graphene.relay.Node, )

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_parts = SQLAlchemyConnectionField(Part.connection)
    parts_by_category = graphene.List(Part, category=graphene.String())

    def resolve_parts_by_category(self, info, category=None):
        query = Part.get_query(info)  # SQLAlchemy query
        if category:
            return query.filter(PartModel.category == category).all()
        return query.all()

schema = graphene.Schema(query=Query)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
