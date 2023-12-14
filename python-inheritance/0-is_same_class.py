'''create a class Similar to hold our funtion define a function that '''
class Myclass:
  pass
def is_instance_of_class(obj, cls):
    '''cls stands for class,obj object
       In this function, obj is the object we want to check, and cls is the class we want to check against. 
       The function first checks if obj is an instance of cls using isinstance(). If it is,
       the function then checks if the type of obj is exactly equal to cls using the type() function. 
       If both conditions are true, the function returns True, 
       indicating that obj is exactly an instance of cls. else, the function returns False
    '''
    return isinstance(obj, cls) and type(obj) == cls
    '''returns true or false'''

'''create a class'''
def is_same_class(obj, a_class):
      a=1
      if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
      elif is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
      if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
         