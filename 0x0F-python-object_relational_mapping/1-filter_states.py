#!/usr/bin/python3

""" lists all states with name starting with N from database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states WHERE `name` LIKE "N%" ORDER BY `id`')
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
