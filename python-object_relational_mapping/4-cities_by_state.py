import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    db_name = argv[3]
    # statename_searched = input("enter state name:  ")
    

    conn = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_passwd, port=3306, db=db_name)
    cursor = conn.cursor()
    query = """SELECT cities.id,cities.name, states.name
               FROM cities
               INNER JOIN states ON
               cities.state_id=states.id
                ORDER BY cities.id"""
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()