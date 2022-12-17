# Write your test here
import pytest
from challenge01 import *

def test_breadth_first_traversal():
    graph = Graph()

    a = graph.add_node("A")
    b = graph.add_node("B")
    c = graph.add_node("C")
    d = graph.add_node("D")
    e = graph.add_node("E")
    f = graph.add_node("F")
    g = graph.add_node("G")
    h = graph.add_node("H")
    i = graph.add_node("I")
    k = graph.add_node("K")

    graph.add_edge( a,  b)
    graph.add_edge( a,  c)
    graph.add_edge( a,  e)

    graph.add_edge( b,  d)

    graph.add_edge( c,  f)

    graph.add_edge( e,  d)
    graph.add_edge( e,  f)
    graph.add_edge( e,  g)

    graph.add_edge( f,  h)
    graph.add_edge( f,  i)

    graph.add_edge( g, h)

    graph.add_edge( h, k)

    graph.add_edge( i, k)

    result = graph.breadth_first_traversal(a)

    list=[]
    for value in result:
        list.append(value.__str__())
    actual=list

    extcepted = ["A", "B", "C", "E", "D", "F", "G", "H", "I", "K"]
    assert actual == extcepted