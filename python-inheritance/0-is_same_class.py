'''create a class Similar to hold our funtion define a function that '''
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

