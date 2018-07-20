#!/usr/bin/python3
"""Script lists all states from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) > 3:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
        query_rows = cursor.fetchall()
        for row in query_rows:
            print(row)
        cursor.close()
        db.close()
