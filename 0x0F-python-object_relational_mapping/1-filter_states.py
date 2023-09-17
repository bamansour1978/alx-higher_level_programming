#!/usr/bin/python3

"""1-filter_states.py
"""

if __name__ == "__main__":
    import sys
    import MySQLdb

    db_host = "localhost"
    db_user = sys.argv[1]  # "username"
    db_password = sys.argv[2]  # "password"
    db_name = sys.argv[3]  # "database_name"
    port = 3306

    db = MySQLdb.connect(
        host=db_host, user=db_user, passwd=db_password, db=db_name, port=port
    )
    c = db.cursor()

    c.execute("SELECT * FROM states WHERE name \
LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for r in rows:
        print(r)

    c.close()
    db.close()
