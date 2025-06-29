#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a' from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    # Create engine to connect to the MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Start a session
    session = Session(engine)

    # Query State objects that contain the letter 'a' in their name
    states = session.query(State).filter(State.name.like('%a%'))\
                    .order_by(State.id).all()

    # Print results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
