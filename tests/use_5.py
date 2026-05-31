import time

from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import Hydrogen_Bonds, Hydrogen_Bond, Colvars_Lists

st = time.time()
file_path = r"file.xyz"

xyz_tr = XYZ_Trajectory.extr_from_xyz(file_path=file_path)
hbs1_list = []
hbs2_list = []
for mol in xyz_tr.steps:
    mol = mol.atoms
    hbs1_list.append(Hydrogen_Bond([mol[26], mol[2], mol[1]]))
    hbs2_list.append(Hydrogen_Bond([mol[27], mol[5], mol[4]]))

hbs1_list = Hydrogen_Bonds(hbs1_list)
hbs2_list = Hydrogen_Bonds(hbs2_list)
clv1 = hbs1_list.colvars_list
clv2 = hbs2_list.colvars_list

ft = time.time()

clvs = Colvars_Lists([clv1.colvars_lsts, clv2.colvars_lsts])
clvs.colvars_plot()

file_path = r"file1.xyz"

xyz_tr = XYZ_Trajectory.extr_from_xyz(file_path=file_path)
hbs_list = []

for mol in xyz_tr.steps:
    mol = mol.atoms
    hbs_list.append(Hydrogen_Bond([mol[4], mol[5], mol[1]]))

hbs_list = Hydrogen_Bonds(hbs_list)
clv = hbs_list.colvars_list
clv.colvars_plot()

file_path = r"file2.xyz"

xyz_tr = XYZ_Trajectory.extr_from_xyz(file_path=file_path)
hbs_list = []

for mol in xyz_tr.steps:
    mol = mol.atoms
    hbs_list.append(Hydrogen_Bond([mol[1], mol[2], mol[26]]))

hbs_list = Hydrogen_Bonds(hbs_list)
clv = hbs_list.colvars_list
clv.colvars_plot()

file_path = r"file3.xyz"

xyz_tr = XYZ_Trajectory.extr_from_xyz(file_path=file_path)
hbs_list = []

for mol in xyz_tr.steps:
    mol = mol.atoms
    hbs_list.append(Hydrogen_Bond([mol[4], mol[2], mol[1]]))

hbs_list = Hydrogen_Bonds(hbs_list)
clv = hbs_list.colvars_list
clv.colvars_plot()

ft = time.time()

print(ft-st)
