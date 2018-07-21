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
    for states in session.query(State).order_by(State.id).limit(1).all():
        print("{}: {}".format(states.id, states.name))
    session.close()
