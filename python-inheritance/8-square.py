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