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
    def __str__(self):
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
    def __dir__(self):
     return sorted(
        ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
         '__eq__', '__format__', '__ge__', '__getattribute__', 
         '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
           '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
           '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
             'area', 'integer_validator']
     )