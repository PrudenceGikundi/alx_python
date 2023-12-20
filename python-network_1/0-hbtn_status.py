'''import request'''
import requests

'''takes the url and request it using the get method'''
url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print("Body request:")
print("\t- type: {}".format(type(response.text)))
print("\t- content: {}".format(response.text))