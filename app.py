from flask import Flask
from database import init_db, db_session
from flask_graphql import GraphQLView
from schema import schema 

app = Flask(__name__)
app.debug = True
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
default_query = '''
{
  allProfessors{
    edges {
      node {
        id,
        name,
        department {
          id,
          name
        },
        role {
          id,
          name
        }
      }
    }
  }
}'''.strip()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # for having the GraphiQL interface
    )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    init_db()
    app.run()

