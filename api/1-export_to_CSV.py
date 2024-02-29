import requests
import sys
import csv

url = "https://jsonplaceholder.typicode.com/users"
user_id = sys.argv[1]
endpoint1 = f"{url}/{user_id}"
endpoint2 = f"{url}/{user_id}/todos"

response1 = requests.get(url=endpoint1)
response2 = requests.get(url=endpoint2)

data1 = response1.json()
data2 = response2.json()
myarray = []
csvheader = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']

for task in data2:  # Iterate over tasks from the second endpoint
    listing = [task['userId'], data1['username'], task['completed'], task['title']]
    myarray.append(listing)

with open("USER_ID.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(myarray)

print("done")


# print('completed')
# print(f"Employee {name} is done with tasks({completed_task}/{total_tasks}):")

# for i in completed:
#   print(f"\t {i}")
