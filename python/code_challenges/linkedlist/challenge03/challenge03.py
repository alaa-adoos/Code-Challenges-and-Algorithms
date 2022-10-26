# Write here the code challenge solution



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
    
    def removeNthFromEnd(self,n):
        '''
        remove the n of the end list and retrun it's head
        if linked list have one Node return None
        if n>0  take to pointer left and right and the difference between them is n 

        
        '''
        
        right=self.head
        left=self.head
        if right.next is None:
            self.head=self.head.next
            return self.head
        while n>0 and right:
            right=right.next
            n-=1
        while right.next:
            left=left.next
            right=right.next

        left.next=left.next.next

        return self.head
   
    
if __name__ == "__main__":
    llist = LinkedList()
    node1 =llist.append(5)
    node2 =llist.append(4)
    node3 =llist.append(3)
    node4 =llist.append(2)
    node5 =llist.append(1)
    print ("Created Linked List: ")
    print(llist.__str__())#[1, 2, 3, 4, 5]
    llist.removeNthFromEnd(2)
    print(llist.__str__())#[1, 2, 3, 5]
