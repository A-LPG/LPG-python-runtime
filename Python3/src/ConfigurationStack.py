
from typing import Sized
from ConfigurationElement import  ConfigurationElement  
from StateElement import  StateElement  
from ObjectTuple import  ObjectTuple  
from ParseTable import  ParseTable  

class ConfigurationStack(object): 

    TABLE_SIZE: int = 1021# 1021 is a prime

    def __init__(self,prs: ParseTable): 
        self.prs = prs
        self.state_element_size : int = 1
        self.state_root =  StateElement()
       
        self.state_root.number = prs.getStartState()
    
        self.table =  [None]* ConfigurationStack.TABLE_SIZE
        self.configuration_stack: ObjectTuple =  ObjectTuple(1 << 12)
        self.max_configuration_size: int=0
        self.stacks_size: int=0

    
    def makeStateList(self,parent: StateElement, stack, index: int, stack_top: int) -> StateElement: 
        i: int = index
        while ( i <= stack_top ): 

            self.state_element_size+=1

            state: StateElement =  StateElement()

            state.number = stack[i]
            state.parent = parent

            parent.children = state

            parent = state
            i+=1

        return parent
    
    def findOrInsertStack(self,root: StateElement, stack, index: int, stack_top: int) -> StateElement : 
        state_number: int = stack[index]
        p: StateElement  = root 
        while ( p != None ): 
            if (p.number == state_number): 
                if index == stack_top :
                    return p 
                else:
                    if p.children == None:
                        return self.makeStateList(p, stack, index + 1, stack_top)   
                    else:
                        return self.findOrInsertStack(p.children, stack, index + 1, stack_top)
            
            p = p.siblings

        self.state_element_size+=1

        node: StateElement =  StateElement()
        node.int = state_number
        node.parent = root.parent
        node.children = None
        node.siblings = root.siblings
        root.siblings = node

        return node  if index == stack_top  else  self.makeStateList(node, stack, index + 1, stack_top)
    
    def findConfiguration(self,stack, stack_top: int, curtok: int) -> bool: 

        last_element: StateElement = self.findOrInsertStack(self.state_root, stack, 0, stack_top)

        hash_address: int = curtok % ConfigurationStack.TABLE_SIZE
        configuration: ConfigurationElement = self.table[hash_address]  
        while configuration: 
            
            if (configuration.curtok == curtok and last_element == configuration.last_element): 
                return True 
            configuration = configuration.next

        return False
    

    def push(self,stack, stack_top: int, conflict_index: int, curtok: int, action_length: int) -> None: 

        configuration: ConfigurationElement =  ConfigurationElement()
        hash_address: int = curtok % ConfigurationStack.TABLE_SIZE

        configuration.next = self.table[hash_address]

        self.table[hash_address] = configuration
        self.max_configuration_size+=1# keep track of int of configurations

        configuration.stack_top = stack_top
        self.stacks_size += (stack_top + 1) # keep track of int of stack elements processed
        configuration.last_element = self.findOrInsertStack(self.state_root, stack, 0, stack_top)
        configuration.conflict_index = conflict_index
        configuration.curtok = curtok
        configuration.action_length = action_length

        self.configuration_stack.add(configuration)
        return
    
    def pop(self) -> ConfigurationElement:
     
        if self.configuration_stack.size() > 0 : 
            index: int = self.configuration_stack.size() - 1
            configuration : ConfigurationElement =self.configuration_stack.get(index)
            configuration.act = self.prs.baseAction(configuration.conflict_index)
            configuration.conflict_index+=1
            if (self.prs.baseAction(configuration.conflict_index) == 0): 
                self.configuration_stack.reset(index)
            
            return configuration
        else :
            return  None
        
    
    def top(self) -> ConfigurationElement: 
       
        if (self.configuration_stack.size() > 0): 
           
            index: int = self.configuration_stack.size() - 1
            configuration : ConfigurationElement=self.configuration_stack.get(index)
            configuration.act = self.prs.baseAction(configuration.conflict_index)
            return configuration
        else :
            return None
        
       
    
    def size(self) -> int : 
        return self.configuration_stack.size()
    
    def maxConfigurationSize(self)-> int : 
        return self.max_configuration_size
    
    def numStateElements(self)-> int : 
        return self.state_element_size
    
    def stacksSize(self)-> int : 
        return self.stacks_size
    

