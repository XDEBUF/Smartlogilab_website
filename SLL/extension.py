from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from flask_login import LoginManager
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy import select
import os
from dotenv import load_dotenv
#basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()
login_manager = LoginManager()
metadata = MetaData()
database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise ValueError("La variable d'environnement DATABASE_URL n'est pas définie.")
try:
    engine = create_engine(database_url, pool_pre_ping=True)
except Exception as e:
    print(f"Erreur lors de la création de l'engine : {e}")
    raise
try:
    with engine.connect() as connection:
        print("Connection successful")
except Exception as e:
    print(f"Erreur lors de la connexion à la base de données : {e}")
    raise
@event.listens_for(engine, "engine_connect")
def ping_connection(connection, branch):
    if branch:
        # this parameter is always False as of SQLAlchemy 2.0,
        # but is still accepted by the event hook.  In 1.x versions
        # of SQLAlchemy, "branched" connections should be skipped.
        return

    try:
        # run a SELECT 1.   use a core select() so that
        # the SELECT of a scalar value without a table is
        # appropriately formatted for the backend
        connection.scalar(select(1))
    except exc.DBAPIError as err:
        # catch SQLAlchemy's DBAPIError, which is a wrapper
        # for the DBAPI's exception.  It includes a .connection_invalidated
        # attribute which specifies if this connection is a "disconnect"
        # condition, which is based on inspection of the original exception
        # by the dialect in use.
        if err.connection_invalidated:
            # run the same SELECT again - the connection will re-validate
            # itself and establish a new connection.  The disconnect detection
            # here also causes the whole connection pool to be invalidated
            # so that all stale connections are discarded.
            connection.scalar(select(1))
        else:
            raise
Base =declarative_base()
#Base.metadata.create_all(engine)
db = SQLAlchemy()
Session = sessionmaker(bind=engine)