# Write your test here
import pytest
from challenge02 import *


def test_is_Valid_closed_by_same_type_1():
    s = "()"
    actual= is_Valid(s)
    expected =True
    assert actual == expected

def test_is_Valid_closed_by_same_type_2():
    s = "()[]{}"
    actual= is_Valid(s)
    expected =True
    assert actual == expected

def test_is_Valid_closed_by_same_type_3():
    s = "[({}]"
    actual= is_Valid(s)
    expected =False
    assert actual == expected
    
def test_is_Valid_with_another_char():
    s = "[(hello)()]"
    actual= is_Valid(s)
    expected =True
    assert actual == expected

def test_is_Valid_with_another_char_2():
    s = "[{((s))}]"
    actual= is_Valid(s)
    expected =True
    assert actual == expected

def test_is_Valid_in_different_order():
    s = "[{(({)})}]"
    actual= is_Valid(s)
    expected =False
    assert actual == expected

def test_is_Valid_start_with_close_bracket():
    s = "}{(({)})}]"
    actual= is_Valid(s)
    expected =False
    assert actual == expected
    