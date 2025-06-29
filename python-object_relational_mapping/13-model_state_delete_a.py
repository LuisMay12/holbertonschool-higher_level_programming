#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter
    'a' from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL server using SQLAlchemy engine
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    session = Session(engine)

    # Query all State objects whose name contains the letter 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Delete them from the session
    for state in states_with_a:
        session.delete(state)

    # Commit the transaction to apply deletions
    session.commit()

    # Close the session
    session.close()
