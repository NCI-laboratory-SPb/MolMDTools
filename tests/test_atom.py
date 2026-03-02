import pytest

from atom import Atom

def test_atom_distance_0():
    a1 = Atom(coords=[3.1, 55.33, 6.05])
    a2 = Atom(coords=[3.1, 55.33, 6.05])
    assert a1.distance(a2) == 0

def test_atom_distance_1():
    a1 = Atom(coords=[-1.2, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    assert a1.distance(a2) == 2.2

def test_atom_distance_2():
    a1 = Atom(coords=[0, -1.2, 0])
    a2 = Atom(coords=[0, 1, 0])
    assert a1.distance(a2) == 2.2

def test_atom_distance_1():
    a1 = Atom(coords=[0, 0, -1.2])
    a2 = Atom(coords=[0, 0, 1])
    assert a1.distance(a2) == 2.2

def test_atom_angle_0():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 1, 1])
    a3 = Atom(coords=[-4.5, -4.5, -4.5])
    assert Atom.angle(a1, a2, a3) == 0

def test_atom_angle_180():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 1, 1])
    a3 = Atom(coords=[-4.5, -4.5, -4.5])
    assert Atom.angle(a2, a1, a3) == 180

def test_atom_angle_30():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    a3 = Atom(coords=[0.8660254037844386, 0.5, 0])
    assert Atom.angle(a2, a1, a3) == pytest.approx(30.0)

def test_atom_angle_60():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    a3 = Atom(coords=[0.5, 0.8660254037844386, 0])
    assert Atom.angle(a2, a1, a3) == pytest.approx(60.0)

def test_atom_angle_90():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    a3 = Atom(coords=[0, 1, 0])
    assert Atom.angle(a2, a1, a3) == pytest.approx(90.0)

def test_atom_angle_120():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    a3 = Atom(coords=[-0.5, 0.8660254037844386, 0])
    assert Atom.angle(a2, a1, a3) == pytest.approx(120.0)

def test_atom_angle_150():
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    a3 = Atom(coords=[-0.8660254037844386, 0.5, 0])
    assert Atom.angle(a2, a1, a3) == pytest.approx(150.0)

def test_atom_angle_7_5():
    import math
    angle_rad = math.radians(7.5)
    x = math.cos(angle_rad)
    y = math.sin(angle_rad)
    a1 = Atom(coords=[0, 0, 0])
    a2 = Atom(coords=[1, 0, 0])
    a3 = Atom(coords=[x, y, 0])
    assert Atom.angle(a2, a1, a3) == pytest.approx(7.5)