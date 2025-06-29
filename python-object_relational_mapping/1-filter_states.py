#!/usr/bin/python3
"""Lists all states starting with 'N' from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def main():
    """Connects to the database and fetches states starting with 'N'"""
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create cursor and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch and print results
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
