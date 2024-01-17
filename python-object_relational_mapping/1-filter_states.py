import MySQLdb
from sys import argv

if __name__ == '__main__':  # Note the double underscores in __name_

    MySql_username = argv[1]
    MySql_pass = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host='localhost', passwd=MySql_pass, port=3306, user=MySql_username, db=db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM states WHERE LOWER(name) LIKE LOWER("%N%") ORDER BY id ASC')
    rows = cursor.fetchall()

    for row in rows:  # Iterate through each row
        print(row)  # Print the individual row tuple

    cursor.close()
    conn.close()