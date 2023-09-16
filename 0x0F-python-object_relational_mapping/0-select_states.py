#!/usr/bin/python3

""" lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
from sys import argv

if __name__ = "__main__":
    db = MySQLdb.connect(host='127.0.0.1', user=argv[1], passwd=argv[2],
                         db=argv[4], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    states = cursor.fetchall()

    for state in states:
        print(elem)
