import databases
import sqlalchemy


DATABASE_URL = "sqlite:///TestDB.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

events = sqlalchemy.Table(
    "events", metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("id_event", sqlalchemy.Integer()),
    sqlalchemy.Column("event_request", sqlalchemy.String()),
    sqlalchemy.Column("event_response", sqlalchemy.String()),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
