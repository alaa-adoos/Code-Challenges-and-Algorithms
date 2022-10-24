class Node:
    '''
     class Node have a node a vlue and next
    '''
    def __init__(self):
        self.val = None
        self.next = None

class LinkedList:
    '''
     print nodes and remove node between 2 nodes 
    '''
    def __init__(self):
        self.head = None
        self.next = None
    def append(self, new_val):
        node = Node()
        node.val = new_val
        node.next = self.head
        self.head = node
        return self.head
    
    def __str__(self):
            mylist=[]
            current = self.head
            while current:
                mylist.append(current.val)
                current = current.next
                
            return (mylist)

    def middleNode(self):
        mylist=[]
        current=self.head
        while current:
            mylist.append(current.val)
            current=current.next
        return(mylist[len(mylist)//2:])        
    def deleteNode(self,pointer):
        pointer.val = pointer.next.val
        pointer.next = pointer.next.next
   

if __name__ == "__main__":
    llist = LinkedList()
    node1 =llist.append(5)
    node2 =llist.append(4)
    node3 =llist.append(3)
    node4 =llist.append(2)
    node5 =llist.append(1)
    print ("Created Linked List: ")
    print(llist.__str__())
    print("the middle node of the linked list")
    print(llist.middleNode())    
   