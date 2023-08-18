from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from local_settings import postgresql as settings

class DbConnection:
    engine: None
    user: settings.pguser
    passwd: settings.pgpasswd
    host: settings.pghost
    port: settings.pgport
    db: settings.pgdb

    def get_engine(self):
        # hostname is localhost and can be changed
        # given correct network options are selected in docker-compose
        url = f"postgresql://{self.user}:{self.passwd}@{self.host}:{self.port}/{self.db}"
        if not database_exists(url):
            create_database(url)
        self.engine = create_engine(url, pool_size=50, echo=False)
        return self.engine

    def get_session(self):
        session = sessionmaker(bind=self.engine)()
        return session
