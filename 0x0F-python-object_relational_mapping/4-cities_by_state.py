#!/usr/bin/python3
"""
Lists all cities from the database
"""
import MySQLdb
import sys


def list_cities():
    """
    List all cities in the database hbtn_0e_4_usa
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities \
             JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
