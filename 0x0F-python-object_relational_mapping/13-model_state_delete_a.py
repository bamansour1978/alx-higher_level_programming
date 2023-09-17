#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select, insert

if __name__ == "__main__":
    engne = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )

    Sess = sessionmaker(bind=engne)
    sess = Sess()
    deleteStates = sess.query(State).filter(State.name.like(f'%a%')).all()
    if deleteStates:
        for state in deleteStates:
            sess.delete(state)
        sess.commit()

    sess.close()
