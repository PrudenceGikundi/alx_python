'''a script that starts a Flask web application'''
from flask import Flask
'''creating an instance of the class '''
app= Flask(__name__)
@app.route("")
def hello_world():
  return "Hello HBNB!"