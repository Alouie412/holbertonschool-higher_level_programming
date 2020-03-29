#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
#from sqlalchemy.orm import sessionmaker


def listStateObj():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

#    This works, but does not give the exact output we want

    q = engine.execute('SELECT * FROM states')
    available_tables = q.fetchall()
#    print(available_tables)

    for x in available_tables:
        print("{}: {}".format(x.id, x.name))


#    Base.metadata.create_all(engine)

if __name__ == '__main__':
    listStateObj()
