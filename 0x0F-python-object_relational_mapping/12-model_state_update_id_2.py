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

    session.query(State).filter(State.id == '2').update({'name': 'New Mexico'})
    session.commit()
    session.close()
