'''import requests and sys'''
import sys
import requests
'''taking a url from the command line arguments using the sys'''
url = sys.argv[1]
'''return the response from the server'''
response = requests.get(url)
'''check if the variable X-Request-Id is in the header '''
if 'X-Request-Id' in response.headers:
  value = response.headers['X-Request-Id']
  print(value)