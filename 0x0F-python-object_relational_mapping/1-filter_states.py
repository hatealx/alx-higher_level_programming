#!/usr/bin/python3
"""list all states start with N"""
import MySQLdb
import sys


def list_states_with_n():
    """
    list all states starting with N
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()

    # Execute the query to select states starting with N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all the rows from the query result
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states_with_n()
