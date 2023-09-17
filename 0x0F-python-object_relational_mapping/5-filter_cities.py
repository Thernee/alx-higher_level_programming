#!/usr/bin/python3

""" lists all cities from the database hbtn_0e_4_usa."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    query = "SELECT cities.name\
        FROM cities INNER JOIN states ON cities.state_id=states.id\
        WHERE states.name = %s ORDER BY cities.id"
    cursor.execute(query, (argv[4],))
    cities = cursor.fetchall()

    # for city in cities:
    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
