import numpy as np
import pytest

from molmdtools.atom import Atom
from molmdtools.molecule import Molecule, Dist_Matrix

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

def test_molecule_plus_molecule():
    a0 = Atom(coords=[0, 0, 0])
    a1 = Atom(coords=[1, 1, 1])
    a2 = Atom(coords=[1, -1, -1])
    a3 = Atom(coords=[2, 1, 0])
    mol1 = Molecule([a0, a1])
    mol2 = Molecule([a2, a3])
    mol3 = Molecule([a0, a1, a2, a3])
    atoms_coords_1 = [x.coords for x in (mol1 + mol2).atoms]
    atoms_coords_2 = [x.coords for x in mol3.atoms]
    assert atoms_coords_1==atoms_coords_2

def test_molecule_getitem():
    a0 = Atom(coords=[0, 0, 0])
    a1 = Atom(coords=[1, 1, 1])
    a2 = Atom(coords=[1, -1, -1])
    a3 = Atom(coords=[2, 1, 0])
    mol = Molecule(atoms=[a0, a1, a2, a3])
    assert mol[0] is a0
    assert mol[3] is a3

def test_molecule_setattr():
    a0 = Atom(coords=[0, 0, 0])
    a1 = Atom(coords=[1, 1, 1])
    a2 = Atom(coords=[1, -1, -1])
    a3 = Atom(coords=[2, 1, 0])
    mol_ref = Molecule(atoms=[a0, a3, a2])
    mol = Molecule(atoms=[a0, a1, a2])
    mol[1] = a3
    assert mol.atoms==mol_ref.atoms

def test_molecule_delattr():
    a0 = Atom(coords=[0, 0, 0])
    a1 = Atom(coords=[1, 1, 1])
    a2 = Atom(coords=[1, -1, -1])
    a3 = Atom(coords=[2, 1, 0])
    mol_ref = Molecule(atoms=[a0, a2, a3])
    mol = Molecule(atoms=[a0, a1, a2, a3])
    del mol[1]
    assert mol.atoms==mol_ref.atoms