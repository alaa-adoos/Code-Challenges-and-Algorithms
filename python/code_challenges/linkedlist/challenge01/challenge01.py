
class Node:
    '''   
     take Node data and next 
    '''
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    '''
    take head of linkedlist
    and methods that do a print nodes or delete node 
    '''
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        '''
         insert a new node 
        '''
        
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode    


    def delete(self,node):
        '''
         take  node data as argument and remove it
        '''
        currentNode=self.head

        while True:
            if currentNode.data==node:
                previousNode.next=currentNode.next
                currentNode.next==None
                break

            previousNode=currentNode    
            currentNode=currentNode.next    


    def print_list(self):
          '''
          print each data node in list []
          
          '''

          currentNode=self.head
          data=[] 
          while True:
            if currentNode is None:
                break
            data.append(currentNode.data)
            currentNode=currentNode.next
          return data  


