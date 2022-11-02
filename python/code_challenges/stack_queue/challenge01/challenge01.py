# Write here the code challenge solution
class Node:
    """
    Node class to make a node and it take a value for the node
    """
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue



class Stack:
    """
    Stack class have method for push, pop, peek,empty
    """

    def __init__(self):
        """
        constructor that have top and size
        """
        self.top = None
        self.size = 0

    def push(self,value):
        """
        take a node and put in in stack

        Args:
            value (node): the value of node 
        """
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        """
         pop function is a function that take the node and delete it from the Stack

        Returns:
            the value of deleted node
            if the stack is empty return string
        """

        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This is empty")
    
    def peek(self):
        """
       peek to  get the top value 

        Returns:
            the top value or string of stack is empty 
        """

        if self.top:
            return self.top.value
        else:
            return("This is empty")

    def get_size(self):
        """
         method to get size of stack
        Returns:
            int: size of stack
        """
        return self.size




class MyQueue():
    """
    Queue that implement two stack 
    """
    def __init__(self):
        self.stack_push = Stack()
        self.stack_pop = Stack()

    def push(self,value):
        """
         push method take a node and put it in the stack_push 
        Args:
            value (node)

        Returns:
            stack
        """
        if self.stack_pop.get_size()!=0 :
            for i in range(self.stack_pop.get_size()):
                self.stack_push.push(self.stack_pop.pop())

        return self.stack_push.push(value)


    def pop(self):
        """
        pop method is a method that push the element to stack_pop then remove the first element to achieve FIFO 
        Returns:
          stack
        """
        if self.stack_push.get_size()!=0 :
            for i in range(self.stack_push.get_size()):
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()


    def peek(self):
        """
        peek to  get the top value 

        Returns:
            the top value or string of stack is empty 
        """
        if self.stack_push.get_size()==0 :
            return self.stack_pop.peek()
        else :
            for i in range(self.stack_push.get_size()):
                self.stack_pop.push(self.stack_push.pop())
            return self.stack_pop.peek()

    def empty(self):
        """
         check if the stack is empty
        Returns:
            boolean
        """
        return self.stack_push.get_size()==0 and self.stack_pop.get_size()==0
             