'''Write a Python script that takes in a URL, sends a request
 to the URL and displays the body of the response.

If the HTTP status code is greater than or equal to 400, 
print: Error code: followed by the value of the HTTP status code
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys
You don’t need to check arguments passed to the script (number or type)'''


'''importing the sys and requests packages'''
import requests
import sys

'''variable to store the url'''
url=sys.argv[1]

'''sending a request to the url and checking for errors'''
response = requests.get(url=url)
if response.status_code >= 400:
  print("error code: {}".format(response.status_code))
else:
  print(response.text)