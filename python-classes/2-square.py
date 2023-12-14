'''create a class Square'''
class Square:
  '''class that defines properties of a square'''
  def __init__(self, size):
    '''create an instance of a class using the init constructor'''
    size.__size= size

    if not isinstance(size, int):
      raise TypeError("SIZE MUST AN INTEGER")
    elif size<0:
      raise ValueError("size must be >=0")
    else:
      size.__size=size
  def area(self):
    return self.__size**2
