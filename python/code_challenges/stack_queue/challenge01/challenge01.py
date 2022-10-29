# Write here the code challenge solution
class Node:
    #Node class to make a node and it take a value for the node
    def __init__(self,vlaue):
        self.next = None
        self.value = vlaue



class Stack:
    #Stack class have method for push, pop, peek,empty

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,value):
    #push method take a node and put it in the Stack
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
    # pop function is a function that take the node and delete it from the Stack

        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.value
        else:
            return("This is empty")
    
    def peek(self):
    #peek method value for node and get it 

        if self.top:
            return self.top.value
        else:
            return("This is empty")

    def get_size(self):
    # return the size of the stack
        return self.size




class MyQueue():
    #MyQueue class use 2 stack to make Queue
    def __init__(self):
        # Implement a first in first out (FIFO) queue using only two stacks
        self.stack_push = Stack()
        self.stack_pop = Stack()

    def push(self,value):
    #push method take a node and put it in the stack_push 
        if self.stack_pop.get_size()!=0 :
            for i in range(self.stack_pop.get_size()):
                self.stack_push.push(self.stack_pop.pop())

        return self.stack_push.push(value)


    def pop(self):
    # pop method is a method that push the element to stack_pop then remove the first element to achieve FIFO 
        if self.stack_push.get_size()!=0 :
            for i in range(self.stack_push.get_size()):
                self.stack_pop.push(self.stack_push.pop())
        return self.stack_pop.pop()


    def peek(self):
    #peek method value for node and get it 
        if self.stack_push.get_size()==0 :
            return self.stack_pop.peek()
        else :
            for i in range(self.stack_push.get_size()):
                self.stack_pop.push(self.stack_push.pop())
            return self.stack_pop.peek()

    def empty(self):
    # return true if the stack is empty
        return self.stack_push.get_size()==0 and self.stack_pop.get_size()==0
             