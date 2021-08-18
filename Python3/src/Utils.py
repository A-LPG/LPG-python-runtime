

def arraycopy(src, srcPos: int, dest, destPos: int, numElements: int): 
    for i in range(numElements):
        dest[destPos + i] = src[srcPos + i]
    return dest
                    

class ArrayList(object):
    def __init__(self):
       self.content = []

    def clone(self):
        result =   ArrayList()
        for i in range(len(self.content)):
            result.content.append(self.content[i])
        
        return result
    
    def addAll(self,index, vals=None):  
        tempArray = []
        if vals != None : 
            if  isinstance(vals,ArrayList):
                tempArray = vals.toArray()
            elif isinstance(vals,list):
                tempArray = vals
            else:
                raise ValueError

            for i in range( tempArray) :
                self.add(index,tempArray[i])    
            return True
        else :
            if  isinstance(index,ArrayList):
                tempArray = index.toArray()
            elif isinstance(index,list):
                tempArray = index
            else:
                raise ValueError
            tempArray = index.toArray()
            for i in range( tempArray) :
                self.content.append(tempArray[i])
            
        return True
        
    

    def clear(self): 
        self.content = []
    
    def remove(self,indexOrElem): 
        self.content.remove(indexOrElem)
        return True
    

    def removeAll(self):  
        self.content = []
        return True
    

    def toArray(self):   
        result =[]  
        for x in result :
            result.append(x)

        return result
    

    def size(self): 
        return len(self.content)
    

    def add(self,index, elem=None): 
        if (elem != None): 
            temp =[]
            temp = self.content[: index]
            temp.append= elem
            for x in self.content[index:]:
                temp.append(x)
            self.content = temp
        else :
            self.content.append(index)
        
    

    def get(self, index: int): 
        return self.content[index]
    

    def contains(self,val):  
        for x in self.content:
            if x == val:
                return True
        return False
 
    def containsAll(self,elems):  
        return False
    

    def isEmpty(self):  
        return self.size() == 0
    

    def set(self, index: int, element): 
        self.content[index] = element
        return element
    

    def indexOf(self,element): 
        size = self.size()
        for i in range(size):
            if self.content[i] == element:
                return i
        return -1

    

    def lastIndexOf(self,element): 
        size = self.size()
        for i in range(size):
            if self.content[size - i - 1] == element:
                return size - i- i 
        return -1


        

    

        


    


