#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""

import MySQLdb
import sys


def main():
    """
    Connects to the database and fetches states where name matches user input
    """
    username, password = sys.argv[1], sys.argv[2]
    db_name, state_name = sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch and display results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
