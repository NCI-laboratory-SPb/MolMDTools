import numpy as np
import pytest

from atom import Atom
from molecule import Molecule, Dist_Matrix

def test_molecule():
    a0 = Atom(coords=[0, 0, 0])
    a1 = Atom(coords=[1, 1, 1])
    a2 = Atom(coords=[1, 1, -1])

    molecule = Molecule([a0, a1, a2])

    assert molecule.atoms_num == 3

def test_dist_matrix():
    a0 = Atom(coords=[0, 0, 0])
    a1 = Atom(coords=[1, 1, 1])
    a2 = Atom(coords=[1, -1, -1])

    molecule = Molecule([a0, a1, a2])
    dists_matrix = Dist_Matrix(molecule)
    expected = np.array([[0, 1.73, 1.73], [1.73, 0, 2.83], [1.73, 2.83, 0]])
    assert np.allclose(dists_matrix.dist_matrix, expected, atol=0.01)