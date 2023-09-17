#!/usr/bin/python3
""" TASK 16 model state
"""

import sys
from sqlalchemy import create_engine
from relationship_city import City
from relationship_state import State, Base
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engne = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engne)
    Sess = sessionmaker(bind=engne)
    sess = Sess()
    objs = sess.query(State).outerjoin(City).all()
    if objs:
        for state in objs:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")
