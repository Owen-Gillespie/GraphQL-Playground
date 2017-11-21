from flask import Flask
from database import engine, db_session, init_db
from flask_graphql import GraphQLView
from schema2 import schema 

app = Flask(__name__)
app.debug = True
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

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

