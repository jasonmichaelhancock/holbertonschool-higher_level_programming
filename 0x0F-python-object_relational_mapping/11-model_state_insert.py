#!/usr/bin/python3
"""script that adds the State object Louisiana to the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True, connect_args= dict(port=3306))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newstate = State(name='Louisiana')
    session.add(newstate)
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
