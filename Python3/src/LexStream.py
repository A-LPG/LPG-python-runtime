
from ParseErrorCodes import  ParseErrorCodes
from IMessageHandler import  IMessageHandler  
from IntSegmentedTuple import  IntSegmentedTuple  
from Protocol import  ILexStream, IPrsStream  
import codecs
#
# LexStream contains an array of characters as the input stream to be parsed.
# There are methods to retrieve and classify characters.
# The lexparser "token" is implemented simply as the index of the next character in the array.
# The user must subclass LexStreamBase and implement the abstract methods: getKind.
#
class LexStream ( ILexStream ):
  
    DEFAULT_TAB: int = 1

    def __init__(self,fileName: str, inputChars: str=None, tab: int = DEFAULT_TAB, lineOffsets: IntSegmentedTuple = None): 
        self.index: int = -1
        self.streamLength: int = 0
        self.inputChars: str=""
        self.fileName: str=""
        self.lineOffsets: IntSegmentedTuple
        self.tab: int = self.DEFAULT_TAB

        self.prsStream: IPrsStream = None
        self.errMsg: IMessageHandler = None
        self.lineOffsets =  IntSegmentedTuple(12)
        self.setLineOffset(-1)
        self.tab = tab
        self.initialize(fileName, inputChars, lineOffsets)

    def thisTab(self,tab: int = DEFAULT_TAB):  
        self.lineOffsets =  IntSegmentedTuple(12)
        self.setLineOffset(-1)
        self.tab = tab

    def readDataFrom(self, fileName:str, encoding: str ='ascii', errors:str='strict'):
        # read binary to avoid line ending conversion
        with open(fileName, 'rb') as file:
            bytes = file.read()
            return codecs.decode(bytes, encoding, errors)
    def initialize(self,fileName: str, inputChars: str = None, lineOffsets: IntSegmentedTuple = None): 
        if (None == inputChars): 
            try :
               inputChars= self.readDataFrom(fileName, "ascii")
            except ValueError as  ex:
               pass
          
      
        if (None == inputChars):
            return

        self.setInputChars(inputChars)
        self.setStreamLength(inputChars.__len__())
        self.setFileName(fileName)
        if (lineOffsets): 
            self.lineOffsets = lineOffsets
        else :
            self.computeLineOffsets()
        
    
    def computeLineOffsets(self): 
        self.lineOffsets.reset()
        self.setLineOffset(-1)
        for i in range (0, self.inputChars.__len__()):
            if (ord(self.inputChars[i]) == 0x0A ):
                self.setLineOffset(i)
            
        
    
    def setInputChars(self,inputChars: str): 
        self.inputChars = inputChars
        self.index = -1 # reset the start index to the beginning of the input
    
    def getInputChars(self) -> str: 
        return self.inputChars
    
    def setFileName(self,fileName: str): 
        self.fileName = fileName
    
    def getFileName(self)  -> str: 
        return self.fileName
    
    def setLineOffsets(self,lineOffsets: IntSegmentedTuple): 
        self.lineOffsets = lineOffsets
    
    def getLineOffsets(self)->IntSegmentedTuple :
        return self.lineOffsets
    
    def setTab(self,tab: int): 
        self.tab = tab
    
    def getTab(self) -> int: 
        return self.tab
    
    def setStreamIndex(self, index: int): 
        self.index = index
    
    def getStreamIndex(self)->int: 
        return self.index
    
    def setStreamLength(self,streamLength: int): 
        self.streamLength = streamLength
    
    def getStreamLength(self) -> int: 
        return self.streamLength
    
    def setLineOffset(self,i: int): 
        self.lineOffsets.add(i)
    
    def getLineOffset(self,i: int) -> int: 
        return self.lineOffsets.get(i)
    
    def setPrsStream(self,prsStream: IPrsStream): 
        prsStream.setLexStream(self)
        self.prsStream = prsStream
    
    def getIPrsStream(self) -> IPrsStream :
        return self.prsStream
    

    def orderedExportedSymbols(self) -> list: 
        return []
    
    def getCharValue(self,i: int) ->str :
        return self.inputChars[i]
    
    def getIntValue(self,i: int) -> int : 
        return ord(self.inputChars[i])
    

    def getLineCount(self) -> int : 
        return self.lineOffsets.size() - 1
    
    def getLineNumberOfCharAt(self,i: int) -> int : 
        index: int = self.lineOffsets.binarySearch(i)
        return  -index if index < 0 else ( 1 if index == 0 else index)
    
    def getColumnOfCharAt(self,i: int) -> int : 
        lineNo: int = self.getLineNumberOfCharAt(i)
        start: int = self.lineOffsets.get(lineNo - 1)
        if (start + 1 >= self.streamLength):
            return 1
        for k in range(start+1, i) :
            if (self.inputChars[k] == '\t'): 
                offset: int = (k - start) - 1
                start -= ((self.tab - 1) - offset % self.tab)
            
        
        return i - start
    
    def getToken2(self) -> int : 
         self.index = self.getNext(self.index)
         return self.index
    
    def getToken(self,end_token: int = None ) -> int: 
        if (None == end_token): 
            return self.getToken2()
        
        self.index = (self.getNext(self.index) if self.index < end_token  else self.streamLength)
        return self.index
    
    def getKind(self,i: int) -> int: 
        return 0
    
    def next(self,i: int) -> int : 
        return self.getNext(i)
    
    def getNext(self,i: int) -> int: 
        i+=1
        return (i if i < self.streamLength else self.streamLength)
    
    def previous(self,i: int) -> int : 
        return self.getPrevious(i)
    
    def getPrevious(self,i: int) -> int : 
        return (0 if i <= 0 else  i - 1)
    
    def getName(self,i: int) ->str : 
        return  "" if i >= self.getStreamLength() else  "" + self.getCharValue(i)
    
    def peek(self) -> int : 
        return self.getNext(self.index)
    
    def reset(self,i: int = None): 
        if(i != None):
            self.index = i - 1
        else :
            self.index = -1
        
    
    
    def badToken(self)-> int : 
        return 0
    
    def getLine(self,i: int = None)-> int : 
        if (None != i): 
            return self.getLine2()
        
        return self.getLineNumberOfCharAt(i)
    
    def getLine2(self) -> int : 
        return self.getLineCount()
    
    def getColumn(self,i: int)-> int : 
        return self.getColumnOfCharAt(i)
    
    def getEndLine(self,i: int)-> int : 
        return self.getLine(i)
    
    def getEndColumn(self,i: int)-> int : 
        return self.getColumnOfCharAt(i)
    
    def afterEol(self,i: int) -> bool :
        return (True if i < 1  else  self.getLineNumberOfCharAt(i - 1) < self.getLineNumberOfCharAt(i))
    
    def getFirstErrorToken(self,i: int) -> int : 
        return self.getFirstRealToken(i)
    
    def getFirstRealToken(self,i: int) -> int : 
        return i
    
    def getLastErrorToken(self,i: int) -> int :  
        return self.getLastRealToken(i)
    
    def getLastRealToken(self,i: int) -> int : 
        return i
    
    def setMessageHandler(self,errMsg: IMessageHandler): 
        self.errMsg = errMsg
    
    def getMessageHandler(self) -> IMessageHandler : 
        return self.errMsg
    
    def makeToken(self,startLoc: int, endLoc: int, kind: int): 
        if (self.prsStream): 
            self.prsStream.makeToken(startLoc, endLoc, kind)
        else :
            self.reportLexicalError(startLoc, endLoc)
        
    

    def getLocation(self,left_loc: int, right_loc: int)-> list: 
        length: int = ( right_loc if right_loc < self.streamLength else self.streamLength - 1) - left_loc + 1
        return  [   left_loc,
                    length, 
                    self.getLineNumberOfCharAt(left_loc), 
                    self.getColumnOfCharAt(left_loc),
                    self.getLineNumberOfCharAt(right_loc),
                    self.getColumnOfCharAt(right_loc)
         ]
    
    def reportLexicalError(self,left_loc: int, right_loc: int, errorCode: int = None,
                              error_left_loc_arg: int = None, error_right_loc_arg: int = None, errorInfoArg= None): 

        error_left_loc: int = 0
        if (error_left_loc_arg): 
            error_left_loc = error_left_loc_arg
        
        error_right_loc: int = 0
        if (error_right_loc_arg): 
            error_right_loc = error_right_loc_arg
        
        errorInfo: list =[]
        if (errorInfoArg != None): 
            errorInfo = errorInfoArg
        
        if (None == errorCode): 
            errorCode = (ParseErrorCodes.EOF_CODE if right_loc >= self.streamLength 
                        else ( ParseErrorCodes.LEX_ERROR_CODE if left_loc == right_loc else  ParseErrorCodes.INVALID_TOKEN_CODE))
            tokenText: str = ("End-of-file " if errorCode == ParseErrorCodes.EOF_CODE 
                                             else (           "\"" + self.inputChars[left_loc, left_loc + right_loc - left_loc + 1]  + "\" " 
                                                        if errorCode == ParseErrorCodes.INVALID_TOKEN_CODE 
                                                        else  "\"" + self.getCharValue(left_loc) + "\" "))
            error_left_loc = 0
            error_right_loc = 0
            errorInfo = [tokenText]
        


        if (not self.errMsg): 
            locationInfo: str = self.getFileName() + ':' + self.getLineNumberOfCharAt(left_loc) + ':' + self.getColumnOfCharAt(left_loc) + ':' + self.getLineNumberOfCharAt(right_loc) + ':' + self.getColumnOfCharAt(right_loc) + ':' + error_left_loc + ':' + error_right_loc + ':' + errorCode + ": "
            print("****Error: " + locationInfo)
            if (errorInfo): 
                for i in range(0,errorInfo.__len__()):
                    print(errorInfo[i] + " ")
                
            
            print(ParseErrorCodes.errorMsgText[errorCode])
        else :
            self.errMsg.handleMessage(errorCode, self.getLocation(left_loc, right_loc), self.getLocation(error_left_loc, error_right_loc), self.getFileName(), errorInfo)
        
    
  
    def reportError(self,errorCode: int, leftToken: int, rightToken: int, errorInfo, errorToken: int=0): 
        tempInfo: list=[]
        if ( isinstance(errorInfo, str)): 
            tempInfo = [errorInfo]
        
        elif (isinstance(errorInfo,list)): 
            tempInfo = errorInfo
        
        else :
            tempInfo = []
        
        self.reportLexicalError(leftToken, rightToken, errorCode,  errorToken,errorToken, tempInfo)
    

    def toString(self,startOffset: int, endOffset: int)->str : 
        length: int = endOffset - startOffset + 1
        return ("$EOF" if endOffset >= self.inputChars.__len__() else ( "" if length <= 0 else  self.inputChars[startOffset, startOffset+ length]) )
    


