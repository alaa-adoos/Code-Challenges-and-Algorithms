# Write your test here
import pytest

from challenge01 import TreeNode

def test_zero():
  test = TreeNode()
  actual= test.buildTree([3,9,20,15,7],[9,3,15,20,7])
  excepted= 3
  assert excepted == actual

def test_one():
  test = TreeNode()
  actual= test.findTree([3,9,20,15,7],[9,3,15,20,7])
  excepted= [3, 9, 20, 'null', 'null', 15, 7]
  assert excepted == actual
  
def test_tow():
  test = TreeNode()
  actual= test.buildTree([1],[1])
  excepted= 1
  assert excepted == actual

def test_three():
  test = TreeNode()
  actual= test.findTree([1],[1])
  excepted= [1]
  assert excepted == actual