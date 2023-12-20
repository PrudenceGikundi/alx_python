'''import request'''
import requests

'''takes the url and request it using the get method'''
url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)
print(response.status_code)