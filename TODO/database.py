from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
SQL_ALCHEMY_DATABASE_URL = "sqlite:///./todo.db"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL,connect_args = {"check_same_thread":False})

session = sessionmaker(auto_commit = False,bind = engine,autoflush = False)

Base = declarative_base()
