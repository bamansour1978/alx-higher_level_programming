#!/usr/bin/python3
"""7-model_state_fetch_all.py
"""

from model_state import Base, State
from sqlalchemy import create_engine, select
import sys

if __name__ == "__main__":
    engne = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engne.connect() as connection:
        query = select(State).order_by(State.id.asc())
        states = connection.execute(query)
        for state in states:
            print(f"{state.id}: {state.name}")

    engne.dispose()
