'''create a class Similar to hold our funtion'''
class Similar():
  pass
  '''define a function that '''
  def is_instance_of_class(obj, cls):#cls stands for class,obj object
    return isinstance(obj, cls) and type(obj) == cls

