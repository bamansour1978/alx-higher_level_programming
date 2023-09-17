#!/usr/bin/python3
"""2-my_filter_states.py
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db_host = "localhost"
    db_user = sys.argv[1]  # "username"
    db_password = sys.argv[2]  # "password"
    db_name = sys.argv[3]  # "database_name"
    port = 3306
    state_name = sys.argv[4]  # "database_name"
    query = "SELECT * FROM states WHERE name LIKE BINARY\
 '{}' ORDER BY id ASC".format(state_name)
    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    c = db.cursor()

    c.execute(query)
    rows = c.fetchall()

    for r in rows:
        print(r)

    c.close()
    db.close()
