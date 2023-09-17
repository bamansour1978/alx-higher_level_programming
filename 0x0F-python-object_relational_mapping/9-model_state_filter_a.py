#!/usr/bin/python3
"""9-model_state_filter_a.py
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engne = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engne.connect() as connection:
        query = select(State).order_by(State.id.asc()) \
            .where(State.name.like("%a%"))
        states = connection.execute(query)
        for state in states:
            print(f"{state.id}: {state.name}")

    engne.dispose()
