
import pytest
from challenge02 import *


@pytest.fixture
def linkedList1():

    llist = LinkedList()
    node1 =llist.append(5)
    node2 =llist.append(4)
    node3 =llist.append(3)
    node4 =llist.append(2)
    node5 =llist.append(1)

    return llist.middleNode()

@pytest.fixture
def linkedList2():

    llist = LinkedList()
    node0=llist.append(6)
    node1 =llist.append(5)
    node2 =llist.append(4)
    node3 =llist.append(3)
    node4 =llist.append(2)
    node5 =llist.append(1)

    return llist.middleNode()
    



def test_Middle_node_1(linkedList1):
    actual = linkedList1
    expected =  [3,4,5]
    assert actual == expected
    
def test_Middle_node_2(linkedList2):
    actual = linkedList2
    expected = [4,5,6]
    assert actual == expected
    