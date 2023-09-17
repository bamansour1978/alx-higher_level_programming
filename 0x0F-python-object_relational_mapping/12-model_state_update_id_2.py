#!/usr/bin/python3
"""12-model_state_update_id_2.py
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
import sys
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
    updateState = sess.query(State).filter_by(id=2).first()

    if updateState:
        updateState.name = 'New Mexico'
        sess.commit()
    sess.close()
