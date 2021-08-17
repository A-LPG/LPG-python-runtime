 
 
class NullTerminalSymbolsException (Exception ):
    
     
    def __init__(self,info: str = None ): 
        super().__init__()
        if (info == None): 
            self.info = "NullTerminalSymbolsException"
        else :
            self.info = info
        

    def toString(self) -> str: 
        return self.info
    

