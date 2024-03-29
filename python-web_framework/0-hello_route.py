'''a script that starts a Flask web application'''
from flask import Flask
'''creating an instance of the class '''
app= Flask(__name__)
@app.route("/",strict_slashes=False)
# The strict_slashes=False option is used to allow both '/path' and '/path/' to work the same way

#A view function ,hello_world is defined to handle the root route
def hello_world():

  return "Hello HBNB!"
#this condition ensure that the Flask app is run only when the script is executed directly,
# not when it's imported as a module
if __name__=="__main__":
  app.run(host='0.0.0.0',port=5000, debug=True)