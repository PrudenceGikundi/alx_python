'''Write a Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id

You must use Basic Authentication with a personal access token as password to
 access to your information (only read:user permission is needed)
The first argument will be your username
The second argument will be your password (in your case, a personal access token as password)
You must use the package requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)'''

'''import request and sys '''
import requests
from requests.auth import HTTPBasicAuth
import sys


username = sys.argv[1]
access_token = sys.argv[2]

response = requests.get("https://api.github.com/PrudenceGikundi", 
                        auth=HTTPBasicAuth(username, access_token))



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
 