'''importing the base file'''
from models.base import Base
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
    

    '''create getter and setters'''
  @property
  def width(self):
    return self.__width
  @width.setter
  def width(self, value):
    if not isinstance(value, int):
      raise TypeError("width must be an integer")
    if value <= 0:
      raise ValueError("width must be > 0")
    self.__width = value

  @property
  def height(self):
    return self.__height
  @height.setter
  def height(self, value):
    if not isinstance(value, int):
      raise TypeError("height must be an integer")
    if value <= 0:
      raise ValueError("height must be > 0")
    self.__height = value
  
  @property
  def x(self):
    return self.__x
  @x.setter
  def x(self, value):
    if not isinstance(value, int):
      raise TypeError("x must be an integer")
    if value < 0:
      raise ValueError("x must be >= 0")
    self.__x = value
  
  @property
  def y(self):
    return self.__y
  @y.setter
  def y(self, value):
    if not isinstance(value, int):
      raise TypeError("y must be an integer")
    if value < 0:
      raise ValueError("y must be >= 0")
    self.__y = value

  def area(self):
    '''defining the area of a rectangle'''
    area = self.__width * self.__height
    return area
  
  def display(self):
    '''defining a function that prints customized printout for x, y '''
    for i in range (self.y):
      print()
      '''updating  x and y such that every time they are called its printed blank'''
    for i in range (self.height):
      print(" " * self.x + "#" * self.width)

  def __str__(self):
    '''this is a string function to overide the printout'''
    return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
  
  def update(self, *args,**kwags):
    '''this is a function that assigns an argument to each attribute:'''
    list=['id','width','height','x','y']
    for i, args in enumerate(args[:5]):
      setattr(self,list[i],args)
      '''kwags arguments'''
    for key, value in kwags.items():
      if key in list:
        setattr(self,key,value)
   


    

    

