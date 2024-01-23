'''a script that starts a Flask web application'''
from flask import Flask
from markupsafe import escape
'''creating an instance of the class '''
app= Flask(__name__)
@app.route("/",strict_slashes=False)
# The strict_slashes=False option is used to allow both '/path' and '/path/' to work the same way

#A view function ,hello_world is defined to handle the root route
def hello_world():

  return "Hello HBNB!"

@app.route("/hbnb")
def hello():
  return "HBNB"

@app.route("/c/<text>")
def hello_again(word):
  return f"C,{escape(word)}"

if __name__=="__main__":
  app.run(host='0.0.0.0',port=5000, debug=True)