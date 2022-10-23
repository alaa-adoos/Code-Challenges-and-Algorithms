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

            
    def deleteNode(self,pointer):
        pointer.val = pointer.next.val
        pointer.next = pointer.next.next


if __name__ == "__main__":
    llist = LinkedList()
    node1 =llist.append(9)
    node2 =llist.append(1)
    node3 =llist.append(5)
    node4 =llist.append(4)
    print ("Created Linked List: ")
    print(llist.__str__())
    llist.deleteNode(node3)
    print("linked list after deletion ")
    print(llist.__str__())