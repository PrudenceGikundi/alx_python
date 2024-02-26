import requests
import sys
from urllib import response

url="https://jsonplaceholder.typicode.com/users"
user_id=sys.argv[1]
endpoint1= url + "/{}".format(user_id)
endpoint2= url + "/{}".format(user_id) +"/todos"
# print(endpoint)

response1=requests.get(url=endpoint1)
response2=requests.get(url=endpoint2)
# print(response1.json())
# print(response2.json())

data1=response1.json()
data2=response2.json()

name=data1["name"]
total_tasks=len(data2)
completed = [task['title'] for task in data2 if task['completed']]
completed_task=len(completed)


# print('completed')
print(f"Employee {name} is done with tasks({completed_task}/{total_tasks}):")

for i in completed:
  print(f"\t {i}")
