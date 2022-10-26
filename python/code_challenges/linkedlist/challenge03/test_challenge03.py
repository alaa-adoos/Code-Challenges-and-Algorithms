# Write your test here

import pytest
from challenge03 import *


@pytest.fixture
def linkedList1():
    '''
    add head of linkes list then remove n from the end of the list 
    input:[1,2,3,4,5] , n=2
    output:[1,2,3,5]
     
    '''

    llist = LinkedList()
    node1 =llist.append(5)
    node2 =llist.append(4)
    node3 =llist.append(3)
    node4 =llist.append(2)
    node5 =llist.append(1)

    llist.removeNthFromEnd(2)
    return llist.__str__()

@pytest.fixture
def linkedList2():
    '''
    add head of linkes list then remove n from the end of the list 
    input:[1] , n=1
    output:[]
    '''

    llist = LinkedList()
    node =llist.append(1)
    llist.removeNthFromEnd(1)
    return llist.__str__()
    
@pytest.fixture
def linkedList3():
    '''
    add head of linkes list then remove n from the end of the list 
    input:[1,2] , n=1
    output:[1]
    '''
    llist = LinkedList()
    node =llist.append(2)
    node2 =llist.append(1)
    llist.removeNthFromEnd(1)
    return llist.__str__()


 
##############tests############
def test_remove_node_1(linkedList1):
    actual = linkedList1
    expected =  [1,2,3,5]
    assert actual == expected
    
def test_remove_node_2(linkedList2):
    actual = linkedList2
    expected = []
    assert actual == expected

def test_remove_node_3(linkedList3):
    actual = linkedList3
    expected = [1]
    assert actual == expected
