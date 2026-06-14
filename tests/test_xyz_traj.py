import pytest

from molmdtools.atom import Atom
from molmdtools.molecule import Molecule
from molmdtools.xyz_trajectory import XYZ_Trajectory

def test_xyz_tr_extr_from_xyz(tmp_path):
    start_file = "3\ntime\nH    -2.11968    -1.87182    -0.002648\nN    -1.50337    -1.07376    -0.000902\n1    2.00786    -0.173672    -0.000872\n3\ntime\nH    -1.97684    -1.95986    -0.312353\nN    -1.40654    -1.09467    -0.118242\nC    1.95467    -0.123764    0.000745741\n3\ntime\nH    -1.95676    -1.87078    -0.692757\nN    -1.52083    -1.10294    -0.25781\nC    2.11268    -0.0648747    0.109822"
    xyz_file = tmp_path / "trajectory.xyz"
    xyz_file.write_text(start_file)
    tj = XYZ_Trajectory.extr_from_xyz(tmp_path / "trajectory.xyz")
    a1 = Atom(coords=[-2.11968, -1.87182, -0.002648])
    a2 = Atom(coords=[-1.50337, -1.07376, -0.000902])
    a3 = Atom(coords=[2.00786, -0.173672, -0.000872])
    a4 = Atom(coords=[-1.97684, -1.95986, -0.312353])
    a5 = Atom(coords=[-1.40654, -1.09467, -0.118242])
    a6 = Atom(coords=[1.95467, -0.123764, 0.000745741])
    a7 = Atom(coords=[-1.95676, -1.87078, -0.692757])
    a8 = Atom(coords=[-1.52083, -1.10294, -0.25781])
    a9 = Atom(coords=[2.11268, -0.0648747, 0.109822])
    atoms = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
    coords_ref = [atom.coords for atom in atoms]
    mol1_coords = [atom.coords for atom in tj[0].atoms]
    mol2_coords = [atom.coords for atom in tj[1].atoms]
    mol3_coords = [atom.coords for atom in tj[2].atoms]    
    coords = mol1_coords + mol2_coords + mol3_coords
    assert tj.steps_number==3
    assert coords_ref == coords