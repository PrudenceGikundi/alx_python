'''Define a function is_kind_of_class'''
def is_kind_of_class(obj, a_class):
    '''Check whether the object is instance of class or its chidren classes
        returns True if it is 
        return False if its not
    '''
    return isinstance(obj, a_class)