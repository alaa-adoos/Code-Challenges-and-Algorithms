# Write your test here
import pytest
from challenge01 import *

myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
myQueue.push(4)



def test_peek():
    actual= myQueue.peek()
    expected= 1
    assert actual == expected
    
def test_pop():
    actual = myQueue.pop()
    expected = 1
    assert actual == expected
    
def test_empty():
    actual = myQueue.empty()
    expected =False
    assert actual == expected

def test_peek_2():
    actual= myQueue.peek()
    expected= 2
    assert actual == expected

def test_pop_2():
    actual = myQueue.pop()
    expected = 2
    assert actual == expected

def test_pop_3():
    actual = myQueue.pop()
    expected = 3
    assert actual == expected

def test_pop_4():
    actual = myQueue.pop()
    expected = 4
    assert actual == expected

def test_pop_5():
    actual = myQueue.pop()
    expected = "This is empty"
    assert actual == expected

def test_empty_2():
    actual = myQueue.empty()
    expected =True
    assert actual == expected