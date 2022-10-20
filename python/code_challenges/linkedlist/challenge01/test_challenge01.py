# Write your test here
from challenge01 import Node,LinkedList



def insert(): 
        '''
        funcuton to insert a nodes 
        '''
        node1=Node(4)
        node2=Node(5)
        node3=Node(1)
        node4=Node(9)
        myList=LinkedList()
        myList.insert(node1)
        myList.insert(node2)
        myList.insert(node3)
        myList.insert(node4)
        return myList

myList=insert()  
### insertNodes test ### 
def test_insert():
    
       assert myList.print_list()==[4,5,1,9]

#### removeNode test ### 
def test_remove():
        myList.delete(1)
        assert myList.print_list()==[4,5,9]

def test_remove2():
        myList=insert() 
        myList.delete(5)
        assert myList.print_list()==[4,1,9]
