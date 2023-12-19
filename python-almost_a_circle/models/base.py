'''creating our base class'''
class Base:
  '''creating a static attributes which will hold the value 0'''
  __nb_objects=0
  '''creating new instances of our base'''
  def __init__(self, id =None):
    '''check if the instance id is not set to none and return the value of the instance'''
    if id is not None:
      self.id =id
    else:
      '''if it is set to None then the static attribute will be implemented by 1'''
      Base.__nb_objects
