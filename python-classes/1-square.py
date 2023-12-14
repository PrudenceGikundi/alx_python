'''Create a class square'''
class Square:
  '''class that defines properties of a square'''
  def __init__(self, size=0):
    '''create an instance of a class using the init constructor'''
    self.__size=size

    if not isinstance(size, int):
      raise TypeError("SIZE MUST BE AN INTEGER")
      '''checks if the size value is an integer if not it returns a typeError'''
    elif size<0:
      raise ValueError("size must be >=0")
      '''checks if value is < 0 if so it returns a Valueerror'''
    else:
      self.__size=size