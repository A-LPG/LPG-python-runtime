
class UnimplementedTerminalsException (Exception):
    
    def __init__(self,symbols): 
        super().__init__()
        self.symbols = symbols
    
    def getSymbols(self):
        return self.symbols
    

