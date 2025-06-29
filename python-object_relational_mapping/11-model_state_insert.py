#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create connection to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    session = Session(engine)

    # Create new State object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the ID of the new state
    print(new_state.id)

    # Close the session
    session.close()
