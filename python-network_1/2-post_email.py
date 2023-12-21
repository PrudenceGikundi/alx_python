'''Write a Python script that takes in a URL and an email address, 
sends a POST request to the passed URL with the email as a parameter,
 and finally displays the body of the response.

The email must be sent in the variable email
You must use the packages requests and sys
You are not allowed to import packages other than requests and sys'''
'''importing sys and the request package'''
import sys
import requests

'''variables to store a URL and an email address'''
url_to_use = input("Enter URL: ") if len(sys.argv) < 2 else sys.argv[1]
email = input("Enter email: ") if len(sys.argv) < 3 else sys.argv[2]
data_to_be_sent = {
  'email':email
}
'''sending a post request to the URL with the email'''
response = requests.post(url=url_to_use, data=data_to_be_sent)
print(response.text)