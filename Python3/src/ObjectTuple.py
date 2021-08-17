
# This Tuple class can be used to construct a dynamic
# array of integers. The space for the array is allocated in
# blocks of size 2**LOG_BLKSIZE. In declaring a tuple the user
# may specify an estimate of how many elements he expects.
# Based on that estimate, suitable values will be calculated
# for log_blksize and base_increment. If these estimates are
# found to be off later, more space will be allocated.
#
from Utils import arraycopy


class ObjectTuple(object): 
    #
    # Constructor of a Tuple
    #
    def __init__(self,estimate: int = 10): 
        self.top : int = 0
        self.array =  [None]*estimate

   
    #
    # This function is used to reset the size of a dynamic array without
    # allocating or deallocting space. It may be invoked with an integer
    # argument n which indicates the  size or with no argument which
    # indicates that the size should be reset to 0.
    #
    def reset(self,n: int=0): 
        self.top = n
    
    def capacity(self) -> int : 
        return len(self.array)
    
    #
    # Return size of the dynamic array.
    #
    def size(self) -> int : 
        return self.top
    

    #
    # Return a reference to the ith element of the dynamic array.
    #
    # Note that no check is made here to ensure that 0 <= i < top.
    # Such a check might be useful for debugging and a range exception
    # should be thrown if it yields True.
    #
    def get(self,i: int) :
      
        return self.array[i]
    

    #
    # Insert an element in the dynamic array at the location indicated.
    #
    def set(self,i: int, element): 
      
        self.array[i] = element
    

    #
    # Add an element to the dynamic array and return the top index.
    #
    def nextIndex(self) -> int : 
        i: int = self.top
        self.top+=1
        if (i >= self.array.__len__()): 
            self.array= arraycopy(self.array, 0, [None]*(i * 2), 0, i)
        
        return i
    

    #
    # Add an element to the dynamic array and return a reference to
    # that  element.
    #
    def add(self,element): 
        i: int = self.nextIndex()
        self.array[i] = element
    


    

