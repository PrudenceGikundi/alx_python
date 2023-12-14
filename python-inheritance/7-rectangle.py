'''import the 5-base_geometry module'''
BaseGeometry = __import__('5-base_geometry').BaseGeometry
'''create a class rectangle'''
class Rectangle(BaseGeometry):
    '''initialize the width and height variables using init constructor'''
    def __init__(self, width, height):
        
        self.__width =width
        self.__height=height
        self.integer_validator("width",width)
        self.integer_validator("height",height)

        '''function that calculates the area of a rectangle the width and height'''
    def area(self):
        '''return self.__width * self._height'''
        return self.__width * self.__height
    '''string to represent our rectangle '''
    def __string__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
  