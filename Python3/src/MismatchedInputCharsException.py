
class MismatchedInputCharsException (Exception ):
  
     
    def __init__(self,info : str = None): 
        super().__init__()
        if (info == None): 
            self.info = "MismatchedInputCharsException"
        else :
            self.info = info
        
    
    def toString(self) -> str : 
        return self.info
    

