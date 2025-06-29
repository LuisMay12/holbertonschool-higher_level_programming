#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa, with their state names.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the database and retrieves all cities with their states,
    sorted by city id.
    """
    username, password, db_name = sys.argv[1:4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Perform inner join between cities and states
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
