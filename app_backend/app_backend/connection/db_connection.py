from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database
from app_backend.connection.local_settings import postgresql as settings
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float


class DbConnection:
    print(settings)
    engine = None
    user = settings["pguser"]
    passwd = settings["pgpasswd"]
    host = settings["pghost"]
    port = settings["pgport"]
    db = settings["pgdb"]

    def get_engine(self):
        # hostname is localhost and can be changed
        # given correct network options are selected in docker-compose
        url = f"postgresql://{self.user}:{self.passwd}@{self.host}:{self.port}/{self.db}"
        if not database_exists(url):
            create_database(url)
        self.engine = create_engine(url, pool_size=50, echo=False)
        return self.engine

    def get_session(self):
        session = sessionmaker(bind=self.get_engine())()
        return session

    def close_connection(self):
        pass

# The below should go into a separate file for all declarative tables models folder

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=True,
        bind=DbConnection().get_engine()
    )
)
Base = declarative_base()
Base.query = db_session.query_property()


class FoodTruck(Base):
    __tablename__ = "food_truck"

    id = Column(Integer, primary_key=True)
    permit = Column(String, unique=True)
    applicant = Column(String, nullable=False)
    address = Column(String)
    status = Column(String)
    food_items = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)
    zip = Column(Integer)


engine = DbConnection().get_engine()
Base.metadata.create_all(engine)
