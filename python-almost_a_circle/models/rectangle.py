'''importing the base file'''
from base import Base
'''CREATING A CLASS RECTANGLE THAT INHERITS FROM BASE'''
class Rectangle(Base):
  '''creating instance attribute to contain width and height'''
  def __init__(self,width,height, x=0,y=0,id=None):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    '''calling super() function from the base class'''
    super().__init__(id)

    

    

