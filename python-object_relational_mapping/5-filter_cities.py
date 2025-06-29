#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa
Safely avoids SQL injection
"""

import MySQLdb
import sys


def main():
    """
    Connects to the database and lists all cities of the given state,
    ordered by cities.id in ascending order.
    """
    username, password, db_name, state_name = sys.argv[1:5]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()

    # Build the output string of city names
    print(", ".join([row[0] for row in rows]))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
