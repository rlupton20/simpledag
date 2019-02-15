import simpledag
from simpledag import __version__, Dag


def test_version():
    assert __version__ == '0.1.0'


def test_can_add_edge_of_nontrivial_class():
    """Test an edge can be added between non-trivial classes."""
    class Test:
        def __init__(self, v):
            self.v = v

    dag = Dag()
    dag.add_edge(Test(1), Test(2))


def test_children():
    """Test obtaining children of a node in a graph."""
    dag = Dag().add_edge(1,2).add_edge(2,3)
    children = dag.children(1)
    assert 2 in children and 3 not in children


def test_parents():
    """Test obtaining parents of a node in a graph."""
    dag = Dag().add_edge(1,2).add_edge(2,3)
    parents = dag.parents(2)
    assert 1 in parents and 3 not in parents


def test_roots():
    """Test obtaining roots of the graph."""
    dag = Dag().add_edge(1,3).add_edge(2,3).add_edge(4,2)
    roots = dag.roots()
    assert 1 in roots and 4 in roots
    assert 3 not in roots and 2 not in roots


def test_invert():
    """Test inverting a graph."""
    dag = Dag().add_edge(1,2).add_edge(2,3).add_edge(4,2)
    inverse = dag.invert()
    assert inverse.roots() == [3]
    assert set(inverse.children(3)) == set([2])
    assert set(inverse.children(2)) == set([1,4])


def test_closure():
    """Test closure of a set of points in a graph."""
    dag = Dag().add_edge(1,2).add_edge(2,3).add_edge(4,2)
    filtered = simpledag.closure(dag, [1])
    assert 4 not in filtered.nodes


def test_ranked_walk():
    """Test topological walk."""
    dag = Dag().add_edge(1,3).add_edge(2,3).add_edge(4,2)
    for _ in simpledag.ranked_walk(dag):
        pass
