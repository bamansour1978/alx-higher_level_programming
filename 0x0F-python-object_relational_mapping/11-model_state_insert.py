#!/usr/bin/python3
"""11-model_state_insert.py
"""

from model_state import Base, State
from sqlalchemy import create_engine, select, insert
import sys

if __name__ == "__main__":
    engne = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    with engne.connect() as connection:
        trans = connection.begin()
        query = insert(State).values(name="Louisiana")
        connection.execute(query)
        query = select(State).where(State.name == "Louisiana")
        state = connection.execute(query).fetchone()
        if state:
            print(state.id)
        trans.commit()

    engne.dispose()
