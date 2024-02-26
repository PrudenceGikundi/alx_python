import requests
import sys

url="https://jsonplaceholder.typicode.com/users"
user_id=sys.argv[1]
endpoint= url + "/{}".format(user_id) +"/todos"
# print(endpoint)

response=requests.get(url=endpoint)
print(response.json())



