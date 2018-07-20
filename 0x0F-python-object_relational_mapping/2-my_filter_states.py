#!/usr/bin/python3
"""Script lists input state from the database hbtn_0e_0_usa"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) > 4:
        con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
        cursor = con.cursor()
        sql = ("SELECT * FROM states WHERE name='{}'".format(sys.argv[4]))
        cursor.execute(sql)
        while True:
            row = cursor.fetchone()
            if row == None:
                break
            print(row)
        cursor.close()
        con.close()
