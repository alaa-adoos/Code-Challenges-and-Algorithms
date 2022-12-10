
import pytest
from challenge01 import *

@pytest.fixture
def tree1():
    
    tree1=Tree(7)
    tree1.left=Tree(2)
    tree1.right=Tree(9)
    tree1.left.right=Tree(5)
    tree1.left.left=Tree(1)
    tree1.right.right=Tree(14)

    return tree1


def test_two_sum_bst(tree1):
    actual= two_sum_bst(tree1,3)
    extcepted=True
    assert actual == extcepted

def test_two_sum_bst_second(tree1):
    actual= two_sum_bst(tree1,4)
    extcepted=False
    assert actual ==  extcepted