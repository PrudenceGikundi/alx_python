'''a script that starts a Flask web application'''
from flask import Flask
'''creating an instance of the class '''
app= Flask(__name__)
@app.route("/",strict_slashes=False)
def hello_world():
  return "Hello HBNB!"
if __name__=="__main__":
  app.run(host='0.0.0.0',port=5000, debug=True)