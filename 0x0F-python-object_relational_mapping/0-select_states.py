#!/usr/bin/python3

"""Lists all states from the database hbtn_0e_0_usa.
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

    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()

    for r in rows:
        print(r)

    c.close()
    db.close()
