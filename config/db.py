from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'mysql+mysqldb://root:Loki@cat01@host/hogwarts'

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

engine = create_engine('mysql+mysqldb://root:lokicat01@localhost:3306/hogwarts')
meta = MetaData()

conn = engine.connect()