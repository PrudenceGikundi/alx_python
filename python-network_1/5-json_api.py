'''Write a Python script that takes in a letter and sends a POST request
 to http://0.0.0.0:5000/search_user with the letter as a parameter.

The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
Otherwise:
Display Not a valid JSON if the JSON is invalid
Display No result if the JSON is empty
You must use the package requests and sys
You are not allowed to import packages other than requests and sys'''

'''import sys and requests packages'''
import sys
import requests

url= "http://0.0.0.0:5000/search_user"
q = "" if len(sys.argv) == 1 else sys.argv[1]

'''data to be sent to our url'''
payload = {
  'q': q
}

'''post to url'''
response =requests.post(url=url, data=payload)

try:
   check_json = response.json()
   if not check_json:
    print ("No result")
   else:
     id =check_json.get("id")
     name = check_json.get("name")
     print(f"[{id}] {name}")
except ValueError:
  print("Not a valid JSON")
