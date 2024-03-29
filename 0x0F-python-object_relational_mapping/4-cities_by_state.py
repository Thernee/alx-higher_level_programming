#!/usr/bin/python3

""" lists all cities from the database hbtn_0e_4_usa."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
        FROM cities INNER JOIN states ON cities.state_id=states.id\
          ORDER BY cities.id"
    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
