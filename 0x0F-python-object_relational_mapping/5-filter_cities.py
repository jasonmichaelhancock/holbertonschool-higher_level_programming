#!/usr/bin/python3
"""Script lists all cities from the database hbtn_0e_4_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) > 4:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
        cursor = db.cursor()
        cursor.execute("SELECT cities.name, states.name FROM cities JOIN states ON states.id = cities.state_id WHERE states.name =%s ORDER BY cities.id ASC", (sys.argv[4],))
        query_rows = cursor.fetchall()
        list = [];
        for row in query_rows:
            list.append(row[0])
        str = ", ".join(list)
        print(str)
        cursor.close()
        db.close()
