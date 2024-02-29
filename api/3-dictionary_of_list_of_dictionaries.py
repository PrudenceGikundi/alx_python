import MySQLdb
from sys import argv
import json

if __name__ == '__main__':
    mysql_username = argv[1]
    mysql_pass = argv[2]
    db_name = argv[3]

    conn = MySQLdb.connect(host='localhost', passwd=mysql_pass, port=3306, user=mysql_username, db=db_name)
    cursor = conn.cursor()

    # Fetch all tasks from all employees
    cursor.execute('SELECT users.id, users.username, todos.title, todos.completed FROM users JOIN todos ON users.id = todos.userId ORDER BY users.id ASC')
    rows = cursor.fetchall()

    # Structure the data in JSON format
    todo_data = {}
    for row in rows:
        user_id = row[0]
        username = row[1]
        task_title = row[2]
        completed = bool(row[3])

        if user_id not in todo_data:
            todo_data[user_id] = []

        todo_data[user_id].append({"username": username, "task": task_title, "completed": completed})

    cursor.close()
    conn.close()

    # Write JSON data to a file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_data, json_file)
