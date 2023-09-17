#!/usr/bin/python3
"""4-cities_by_state.py
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    db_host = "localhost"
    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    c = db.cursor()

    c.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON states.id = cities.state_id \
    ORDER BY cities.id")
    rows = c.fetchall()

    for r in rows:
        print(r)

    c.close()
    db.close()
