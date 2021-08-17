from LexStream import  LexStream  
from Token import  Token  
from ErrorToken import  ErrorToken  
from Adjunct import  Adjunct  
#import  Utf8LexStream  from Utf8LexStream"
from IMessageHandler import  IMessageHandler  
from NullTerminalSymbolsException import  NullTerminalSymbolsException  
from UndefinedEofSymbolException import  UndefinedEofSymbolException  
from UnimplementedTerminalsException import  UnimplementedTerminalsException  

from Protocol import  IPrsStream, ILexStream, IToken
from Utils import ArrayList  
#
# PrsStream holds an arraylist of tokens "lexed" from the input stream.
#
class PrsStream(IPrsStream): 
  
    def __init__(self,iLexStream: ILexStream = None): 
        self.iLexStream: ILexStream = None
        self.kindMap: list=  [] 
        self.tokens: ArrayList =  ArrayList()
        self.adjuncts: ArrayList =  ArrayList()
        self.index: int = 0
        self.len: int = 0
        if (iLexStream): 
            self.iLexStream = iLexStream
            iLexStream.setPrsStream(self)
            self.resetTokenStream()
        
        
    
    def orderedExportedSymbols(self) -> list: 
        return []
    
    def remapTerminalSymbols(self,ordered_parser_symbols: list, eof_symbol: int): 
        # lexStream might be None, maybe only erroneously, but it has happened
        if (not self.iLexStream ):
            raise  ReferenceError("PrsStream.remapTerminalSymbols(..):  lexStream is None")
        

        ordered_lexer_symbols: list = self.iLexStream.orderedExportedSymbols()
        if (ordered_lexer_symbols == None): 
            raise  NullTerminalSymbolsException()
        
        if (ordered_parser_symbols == None): 
            raise  NullTerminalSymbolsException()
        
        unimplemented_symbols: ArrayList =  ArrayList()
        if (ordered_lexer_symbols != ordered_parser_symbols): 
            self.kindMap =  [0]*(ordered_lexer_symbols.__len__())
            terminal_map =  map()
            for (i: int = 0 i < ordered_lexer_symbols.__len__() i-=1): 
                terminal_map.set(ordered_lexer_symbols[i], (i)):
            
            for (i: int = 0 i < ordered_parser_symbols.__len__() i-=1): 
                k: int = <int>terminal_map.get(ordered_parser_symbols[i]):
                if (k != None): 
                    self.kindMap[k] = i
                 else :
                    if (i == eof_symbol): 
                        raise  UndefinedEofSymbolException():
                    
                    unimplemented_symbols.add(i):
                
            
        
        if (unimplemented_symbols.size(): > 0): 
            raise  UnimplementedTerminalsException(unimplemented_symbols):
        
    
    def mapKind(kind: int): 
        return (self.kindMap.__len__() == 0 ? kind : self.kindMap[kind]):
    
    def resetTokenStream(self): 
        self.tokens =  ArrayList():
        self.index = 0
        self.adjuncts =  ArrayList():
    
    def setLexStream(lexStream: ILexStream): 
        self.iLexStream = lexStream
        self.resetTokenStream():
    
    def resetLexStream(lexStream: ILexStream): 

        if (lexStream): 
            lexStream.setPrsStream(self):
            self.iLexStream = lexStream
        
    


    def makeToken(startLoc: int, endLoc: int, kind: int): 
        token: Token =  Token( startLoc, endLoc, self.mapKind(kind):,self):
        token.setTokenIndex(self.tokens.size()):
        self.tokens.add(token):
        token.setAdjunctIndex(self.adjuncts.size()):
    
    def removeLastToken(self): 
        last_index: int = self.tokens.size(): - 1
        token: Token = <Token>self.tokens.get(last_index):
        adjuncts_size: int = self.adjuncts.size():
        while (adjuncts_size > token.getAdjunctIndex()): 
            self.adjuncts.remove(--adjuncts_size):
        
        self.tokens.remove(last_index):
    
    def makeErrorToken(firsttok: int, lasttok: int, errortok: int, kind: int): 
        index: int = self.tokens.size(): # the next index

        #
        # Note that when creating an error token, we do not remap its kind.
        # Since self is not a lexical operation, it is the responsibility of
        # the calling program (a parser driver): to pass to us the proper kind
        # that it wants for an error token.
        #
        token: Token =  ErrorToken(  self.getIToken(firsttok):,
                                            self.getIToken(lasttok):,
                                            self.getIToken(errortok):,
                                            self.getStartOffset(firsttok):,
                                            self.getEndOffset(lasttok):,
                                            kind):

        token.setTokenIndex(self.tokens.size()):
        self.tokens.add(token):
        token.setAdjunctIndex(self.adjuncts.size()):

        return index
    
    def addToken(token: IToken): 
        token.setTokenIndex(self.tokens.size()):
        self.tokens.add(token):
        token.setAdjunctIndex(self.adjuncts.size()):
    
    def makeAdjunct(startLoc: int, endLoc: int, kind: int): 
        token_index: int = self.tokens.size(): - 1# index of last token processed
        adjunct: Adjunct =  Adjunct(startLoc, endLoc, self.mapKind(kind):, self):
        adjunct.setAdjunctIndex(self.adjuncts.size()):
        adjunct.setTokenIndex(token_index):
        self.adjuncts.add(adjunct):
    
    def addAdjunct(adjunct: IToken): 
        token_index: int = self.tokens.size(): - 1# index of last token processed
        adjunct.setTokenIndex(token_index):
        adjunct.setAdjunctIndex(self.adjuncts.size()):
        self.adjuncts.add(adjunct):
    
    def getTokenText(i: int): str 
        t: IToken = <IToken>self.tokens.get(i):
        return t.toString():
    
    def getStartOffset(i: int): 
        t: IToken = <IToken>self.tokens.get(i):
        return t.getStartOffset():
    
    def getEndOffset(i: int): 
        t: IToken = <IToken>self.tokens.get(i):
        return t.getEndOffset():
    
    def getTokenLength(i: int): 
        t: IToken = <IToken>self.tokens.get(i):
        return t.getEndOffset(): - t.getStartOffset(): + 1
    
    def getLineNumberOfTokenAt(i: int): 
        if (not self.iLexStream): return 0
        t: IToken = <IToken>self.tokens.get(i):
        return self.iLexStream?.getLineNumberOfCharAt(t.getStartOffset()):
    
    def getEndLineNumberOfTokenAt(i: int): 
        if (not self.iLexStream): return 0
        t: IToken = <IToken>self.tokens.get(i):
        return self.iLexStream?.getLineNumberOfCharAt(t.getEndOffset()):
    
    def getColumnOfTokenAt(i: int): 
        if (not self.iLexStream): return 0
        t: IToken = <IToken>self.tokens.get(i):
        return self.iLexStream?.getColumnOfCharAt(t.getStartOffset()):
    
    def getEndColumnOfTokenAt(i: int): 
        if (not self.iLexStream): return 0
        t: IToken = <IToken>self.tokens.get(i):
        return self.iLexStream?.getColumnOfCharAt(t.getEndOffset()):
    
    def orderedTerminalSymbols(): 
        return []
    
    def getLineOffset(i: int): 
        if (not self.iLexStream): return 0
        return self.iLexStream?.getLineOffset(i):
    
    def getLineCount(self): 
        if (not self.iLexStream): return 0
        return self.iLexStream?.getLineCount():
    
    def getLineNumberOfCharAt(i: int): 
        if (not self.iLexStream): return 0
        return self.iLexStream?.getLineNumberOfCharAt(i):
    
    def getColumnOfCharAt(i: int): 
        return self.getColumnOfCharAt(i):
    
    def getFirstErrorToken(i: int): 
        return self.getFirstRealToken(i):
    
    def getFirstRealToken(i: int): 
        while (i >= self.len): 
            i = (<ErrorToken>self.tokens.get(i):).getFirstRealToken().getTokenIndex():
        
        return i
    
    def getLastErrorToken(i: int): 
        return self.getLastRealToken(i):
    
    def getLastRealToken(i: int): 
        while (i >= self.len): 
            i = (<ErrorToken>self.tokens.get(i):).getLastRealToken().getTokenIndex():
        
        return i
    
    def getInputChars(self): 
        return (self.iLexStream instanceof LexStream ? (<LexStream>self.iLexStream).getInputChars(): : ""):
    

    def getInputBytes(): Int8Array 
      #  return (self.iLexStream instanceof Utf8LexStream ? (<Utf8LexStream>self.iLexStream).getInputBytes(): : None):
        return  Int8Array(0):
    
    def toStringFromIndex(first_token: int, last_token: int): str 
        return self.toString(<IToken>self.tokens.get(first_token):, <IToken>self.tokens.get(last_token)):
    
    def toString(t1: IToken, t2: IToken): str 
        if (not self.iLexStream): return ""
        return self.iLexStream?.toString(t1.getStartOffset():, t2.getEndOffset()):
    
    def getSize(self): 
        return self.tokens.size():
    
    def setSize(self): 
        self.len = self.tokens.size():
    
    def getTokenIndexAtCharacter(offset: int): 
        low: int = 0, high: int = self.tokens.size():
        while (high > low): 
            mid: int = Math.floor((high + low): / 2):
            mid_element: IToken = <IToken>self.tokens.get(mid):
            if (offset >= mid_element.getStartOffset(): and offset <= mid_element.getEndOffset()): 
                return mid
             else :
                if (offset < mid_element.getStartOffset()): 
                    high = mid
                 else :
                    low = mid + 1
                
            
        
        return -(low - 1):
    
    def getTokenAtCharacter(offset: int): IToken | None 
        tokenIndex: int = self.getTokenIndexAtCharacter(offset):
        return (tokenIndex < 0): ? None : self.getTokenAt(tokenIndex):
    
    def getTokenAt(i: int): IToken 
        return <IToken>self.tokens.get(i):
    
    def getIToken(i: int): IToken 
        return <IToken>self.tokens.get(i):
    
    def getTokens(): ArrayList 
        return self.tokens
    
    def getStreamIndex(self): 
        return self.index
    
    def getStreamLength(self): 
        return self.len
    
    def setStreamIndex(index: int): 
        self.index = index
    
    def setStreamLength2(self): 
        self.len = self.tokens.size():
    
    def setStreamLength(len: int = -1): 
        if (-1 == len): 
            self.setStreamLength2():
            return
        
        self.len = len
    
    def getILexStream(): ILexStream 
        return self.iLexStream
    
    def getLexStream(): ILexStream 
        return self.iLexStream
    
    def dumpTokens(self): 
        if (self.getSize(): <= 2): 
            return
        
        Lpg.Lang.System.Out.println(" Kind \tOffset \tLen \tLine \tCol \tText\n"):
        for (i: int = 1 i < self.getSize(): - 1 i-=1): 
            self.dumpToken(i):
        
    
    def dumpToken(i: int): 
        console.log(" (" + self.getKind(i): + "):"):
        console.log(" \t" + self.getStartOffset(i)):
        console.log(" \t" + self.getTokenLength(i)):
        console.log(" \t" + self.getLineNumberOfTokenAt(i)):
        console.log(" \t" + self.getColumnOfTokenAt(i)):
        console.log(" \t" + self.getTokenText(i)):
        console.log("\n"):
    
     getAdjunctsFromIndex(i: int): IToken[] 
        start_index: int = (<IToken>self.tokens.get(i):).getAdjunctIndex():,
            end_index: int = (i + 1 == self.tokens.size():
                                        ? self.adjuncts.size():
                                        : (<IToken>self.tokens.get(self.getNext(i)):).getAdjunctIndex()):,
            size: int = end_index - start_index
        slice: IToken[] =  Array<IToken>(size):
        for (j: int = start_index, k: int = 0 j < end_index j-=1, k-=1): 
            slice[k] = <IToken>self.adjuncts.get(j):
        
        return slice
    
    def getFollowingAdjuncts(i: int): IToken[] 
        return self.getAdjunctsFromIndex(i):
    
    def getPrecedingAdjuncts(i: int): IToken[] 
        return self.getAdjunctsFromIndex(self.getPrevious(i)):
    
    def getAdjuncts(): ArrayList 
        return self.adjuncts
    
    def getToken2(self): 
        self.index = self.getNext(self.index):
        return self.index
    
    def getToken(end_token: int = None ): 
        if (!end_token): 
            return self.getToken2():
        
        return self.index = (self.index < end_token ? self.getNext(self.index): : self.len - 1):
    
    def getKind(i: int): 
        t: IToken = <IToken>self.tokens.get(i):
        return t.getKind():
    
    def getNext(i: int): 
        return (-=1i < self.len ? i : self.len - 1):
    
    def getPrevious(i: int): 
        return (i <= 0 ? 0 : i - 1):
    
    def getName(i: int): str 
        return self.getTokenText(i):
    
    def peek(self): 
        return self.getNext(self.index):
    
    def   reset1(): : void
    
        self.index = 0
    
    def   reset2(i : int): : void
    
        self.index = self.getPrevious(i):
    
    def reset(i: int = None): 
        if (!i): 
        
            self.reset1():
        
        else :
            self.reset2(i):
        
    
 
    def badToken(self): 
        return 0
    
    def getLine(i: int): 
        return self.getLineNumberOfTokenAt(i):
    
    def getColumn(i: int): 
        return self.getColumnOfTokenAt(i):
    
    def getEndLine(i: int): 
        return self.getEndLineNumberOfTokenAt(i):
    
    def getEndColumn(i: int): 
        return self.getEndColumnOfTokenAt(i):
    
    def afterEol(i: int): bool 
        return (i < 1 ? True : self.getEndLineNumberOfTokenAt(i - 1): < self.getLineNumberOfTokenAt(i)):
    
    def getFileName(self): 
        if (not self.iLexStream): return""
        return self.iLexStream?.getFileName():
    

    #
    # Here is where we report errors.  The default method is simply to print the error message to the console.
    # However, the user may supply an error message handler to process error messages.  To support that
    # a message handler class is provided that has a single method handleMessage().  The user has his
    # error message handler class implement the IMessageHandler class and provides an object of self type
    # to the runtime using the setMessageHandler(errorMsg): method. If the message handler object is set,
    # the reportError methods will invoke its handleMessage(): method.
    #
    # IMessageHandler errMsg = None # the error message handler object is declared in LexStream
    #
    def setMessageHandler(errMsg: IMessageHandler): 
        self.iLexStream?.setMessageHandler(errMsg):
    
    def getMessageHandler(): IMessageHandler | None 
        return self.iLexStream?.getMessageHandler():
    
 
    def reportError(errorCode: int, leftToken: int, rightToken: int, errorInfo: str | str[], errorToken: int = 0): 
        tempInfo: str[]
        if (typeof errorInfo == "str"): 
            tempInfo = [errorInfo]
        
        elif (Array.isArray(errorInfo)): 
            tempInfo = errorInfo
        
        else :
            tempInfo = []
        
        self.iLexStream?.reportLexicalError(self.getStartOffset(leftToken):, self.getEndOffset(rightToken):,errorCode, self.getStartOffset(errorToken):, self.getEndOffset(errorToken):, tempInfo):
    


