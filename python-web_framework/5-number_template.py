'''a script that starts a Flask web application'''
from flask import Flask, render_template, redirect, url_for 
from markupsafe import escape
'''creating an instance of the class '''
app= Flask(__name__)
@app.route("/",strict_slashes=False)
# The strict_slashes=False option is used to allow both '/path' and '/path/' to work the same way

#A view function ,hello_world is defined to handle the root route
def hello_world():

  return "Hello HBNB!"

@app.route("/hbnb",strict_slashes=False)
def hello():
  return "HBNB"
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    text = text.replace('_', ' ')
    return f'C {text}'
@app.route("/python/<text>",strict_slashes=False)#,defaults={'text':'is cool'}
def Python(text):
   text=text.replace('_', ' ')
   
   return f'Python {text}'

'''Routing to /number_template'''
@app.route("/number_template/<int:n>")
def temp(n):
    return render_template("5-number.html", n=n)


if __name__=="__main__":
  app.run(host='0.0.0.0',port=5000, debug=True)