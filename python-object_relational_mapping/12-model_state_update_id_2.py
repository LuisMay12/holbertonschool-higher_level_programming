#!/usr/bin/python3
"""Updates the name of the State where id = 2 to 'New Mexico' in the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Set up the engine and connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Start a session
    session = Session(engine)

    # Retrieve the state with id=2
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
