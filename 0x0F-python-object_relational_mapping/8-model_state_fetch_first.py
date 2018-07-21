#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True, connect_args= dict(port=3306))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    first = session.query(State).first()
    if (first == None):
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
    session.close()
