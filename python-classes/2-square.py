'''create a class Square'''
class Square:
  '''class that defines properties of a square'''
  def __init__(self, size=0):
    '''create an instance of a class using the init constructor'''
    self.__size= size

    if not isinstance(size, int):
      raise TypeError("size must be an integer")
    elif size < 0:
      raise ValueError("size must be >= 0")
    else:
      self.__size=size
  def area(self):
    return self.__size ** 2
  

