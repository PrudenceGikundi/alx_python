import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    db_name = argv[3]
    statename_searched = argv[4]
    input("The state searched is:  ".format(statename_searched))

    conn = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_passwd, port=3306, db=db_name)
    cursor = conn.cursor()
    query = "SELECT * FROM states WHERE name = %s"
    cursor.execute(query, (statename_searched,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()