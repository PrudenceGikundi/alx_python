'''create a class Square'''
class Square:
  '''class that defines properties of a square'''
  def __init__(self, size):
    '''create an instance of a class using the init constructor'''
    size.__size= size

  def area(self):
    return self.__size**2
  @property
  def size(self):
        """Returns the size of a square"""
        
        return self.__size

  @size.setter
  def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
  def my_print(self):
        """prints in stdout the square with the character #
        
        """

        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))