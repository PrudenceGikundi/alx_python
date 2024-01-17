import MySQLdb
from sys import argv

if __name__== '__main__':

   MySql_username=argv[1]
   MySql_pass= argv[2]
   db_name=argv[3]

   conn= MySQLdb.connect(host='localhost',password=MySql_username,port=3306,username=MySql_username,db=db_name)
   cursor=conn.cursor()
   cursor.execute('SELECT name FROM people WHERE name LIKE "N%" ORDER BY id ASC')
   rows=cursor.fetchall()
   for row in rows:
      print(rows)
   cursor.close()
   conn.close()

