'''import rectangle module and crate a class square that inherits from it'''
from models.rectangle import Rectangle
'''create a class '''
class Square(Rectangle):
  '''a class squre that inherits from Rectangle class'''
  def __init__(self,size,x=0,y=0,id=None):
    self.size= size
    super().__init__(size,size,x,y,id)
  def __str__(self):
   return  f"[Square] ({self.id}){self.x}/{self.y} - {self.size}"
    