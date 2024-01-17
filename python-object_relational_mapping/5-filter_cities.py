import MySQLdb
from sys import argv

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(host='localhost', user=mysql_username, passwd=mysql_passwd, port=3306, db=db_name)
    cursor = conn.cursor()
    query = """SELECT cities.name
               FROM cities
               INNER JOIN states ON
               cities.state_id=states.id
               WHERE states.name = %s
               ORDER BY cities.id ASC
                """
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
    cursor.close()
    conn.close()

    # for i, state in enumerate(states):
    #     print(state[0], end='')
    #     if i < len(states)-1:
    #         print(', ', end='')
    # print('')