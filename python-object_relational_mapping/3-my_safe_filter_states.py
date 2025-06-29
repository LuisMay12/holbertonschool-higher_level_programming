#!/usr/bin/python3
"""Displays all values in the states table where name matches user input,
using parameterized query to prevent SQL injection.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and retrieves states matching a name,
    safely escaping the user input.
    """
    username, password, db_name, state_name = sys.argv[1:5]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
