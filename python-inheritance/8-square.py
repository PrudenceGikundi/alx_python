'''import the 7-base_rectangle'''
Rectangle = __import__('7-rectangle').Rectangle
'''create a square class that inherits rectngle'''
class Square(Rectangle):
   '''initializing size of the square'''
   def __init__(self, size):
      self.__size = size
      self.integer_validator("size", size)
    
   def __str__(self):
      '''returns a string representation of our square'''
      return "[Square] {}/{} {:d}/{:d}".format(self.__size, self.__size) 
   def area(self):
      return self.__size ** 2
   def __dir__(self):
     return sorted(
       ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__',
         '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
         '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
         '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
         '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'area', 'integer_validator']
     )