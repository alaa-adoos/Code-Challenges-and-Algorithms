
import pytest

from challenge02 import *

def test_one():
    # testing repetition
    sen = "ASAC is a department at LTUC. ASAC teaches programming in LTUC."
    actual = repeated(sen)
    expected = "ASAC"
    assert expected == actual

def test_two():
    # testing no repetition
    asd = "I am learning programming at ASAC."
    actual = repeated(asd)
    expected = "No Repetition"
    assert expected == actual

def test_three():
    # testing if it is case sensitive (it is)
    qwe = "Snacks are yummy snacks"
    actual = repeated(qwe)
    expected = "No Repetition"
    assert expected == actual

def test_four():
    # testing if i have empty string 
    gg = ""
    actual = repeated(gg)
    expected = "No Repetition"
    assert expected == actual

def test_five():
    # testing if it is one word 
    aa = "Hello"
    actual = repeated(aa)
    expected = "No Repetition"
    assert expected == actual