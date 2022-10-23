# Write your test here
from challenge01 import Node,LinkedList

def insert():
         '''
         isnert nodes
         '''
         mylist = LinkedList()
         node1 =mylist.append(9)
         node2 =mylist.append(1)
         node3 =mylist.append(5)
         node4 =mylist.append(4)
         return mylist
def delete1():
         '''
         4=>5=>1=>9=>None
         4=>5=>9=>None
         delete node 2
        
         '''
         mylist = LinkedList()
         node1 =mylist.append(9)
         node2 =mylist.append(1)
         node3 =mylist.append(5)
         node4 =mylist.append(4)
         mylist.deleteNode(node2)
         return mylist

def delete2():
         '''
          4=>5=>1=>9=>None  
          4=>1=>9   
          delete node3
          
         '''
         mylist = LinkedList()
         node1 =mylist.append(9)
         node2 =mylist.append(1)
         node3 =mylist.append(5)
         node4 =mylist.append(4)
         mylist.deleteNode(node3)
         return mylist





### insertNodes test ### 
def test_insert():
    
       assert insert().__str__()==[4,5,1,9]

#### removeNode test ### 
def test_remove():
        assert delete1().__str__()==[4,5,9]

def test_remove2():
        assert delete2().__str__()==[4,1,9]
