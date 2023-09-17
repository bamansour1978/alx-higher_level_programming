#!/usr/bin/python3
""" Task 15 model state
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
    newState = State(name='California')
    newCity = City(name='San Francisco', state=newState)

    sess.add_all([newState, newCity])
    sess.commit()
    sess.close()
