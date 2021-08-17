
class StateElement(object):
    def __init__(self): 
      self.parent: StateElement = None 
      self.children: StateElement=None
      self.siblings: StateElement =None
      self.number: int=0

