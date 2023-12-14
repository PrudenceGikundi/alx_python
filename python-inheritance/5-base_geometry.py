'''Define a function BaseGeometry'''
class BaseGeometry:
  '''method raises an exception'''
  def area(self):
     raise Exception("area() is not implemented")
  
  def integer_validator(self, name, value):
     '''if value is not an integer'''
     if not isinstance(value, int):
        raise TypeError("name is not an integer")
     '''if value is <= 0'''
     if value <= 0:
        raise ValueError("name must be greater than 0")    