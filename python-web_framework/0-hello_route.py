'''a script that starts a Flask web application
   Your web application must be listening on 0.0.0.0, port 5000
   must use the option strict_slashes=False in your route definition
'''
#module is documented
from flask import Flask
'''creating an instance of the class '''
app= Flask(__name__)
@app.route("")
def hello_world():
  return "Hello HBNB!"