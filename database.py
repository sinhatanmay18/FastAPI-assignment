from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_Database = 'mysql://{username}:{password}@localhost:{port}/{schema_name}'

engine = create_engine(URL_Database)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

