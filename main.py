import time
from statistics import mean, stdev

import matplotlib.pyplot as plt
import seaborn as sns

from atom import Atom
from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import HB_Analyzer

st = time.time()

traj = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Formimidamid\AIMD\Amidines_S_E-anti_E-anti-pos-1.xyz")
traj5 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Formimidamid\AIMD\FIA_Mark-pos-1.xyz")
traj5.cell = [15.0, 15.0, 15.0]

tj1 = traj

print(len(tj1.steps))

tj1_HB1 = HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[6, 2, 1])
tj1_HB2 = HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[7, 5, 4])

tj1_HB1_and_HB2 = set(tj1_HB1).intersection(set(tj1_HB2))
print(len(tj1_HB1))
print(len(tj1_HB2))
print(f"For my traj HB1 & HB2 steps len: {len(tj1_HB1_and_HB2)}")

tj2 = traj5

print(len(tj2.steps))

tj2_HB1 = HB_Analyzer.hb_in_traj(traj=tj2, atoms_nums=[9, 8, 10])
tj2_HB2 = HB_Analyzer.hb_in_traj(traj=tj2, atoms_nums=[4, 3, 12])

tj2_HB1_and_HB2 = set(tj2_HB1).intersection(set(tj2_HB2))
print(len(tj2_HB1))
print(len(tj2_HB2))
print(f"For traj Mark HB1 & HB2 steps len: {len(tj2_HB1_and_HB2)}")

coll1_file = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Formimidamid\AIMD\Amidines_S_E-anti_E-anti.csv"
coll2_file = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Formimidamid\AIMD\FIA_Mark_AIMD.csv"

clvs = []
HB_cov_dists = []
HB_dists = []
HB_angles = []

for ind, step in enumerate(traj.steps):
    if ind in tj1_HB1_and_HB2:
        atoms = step.atoms
        clv = (atoms[2].distance(atoms[1], cell=[15.0, 15.0, 15.0])-atoms[6].distance(atoms[2], cell=[15.0, 15.0, 15.0]))/2
        clv2 = (atoms[5].distance(atoms[4], cell=[15.0, 15.0, 15.0])-atoms[7].distance(atoms[5], cell=[15.0, 15.0, 15.0]))/2
        clvs.append(clv)
        HB1_cov_dist = atoms[6].distance(atoms[2], cell=[15.0, 15.0, 15.0])
        HB1_dist = atoms[2].distance(atoms[1], cell=[15.0, 15.0, 15.0])
        HB_angles.append(Atom.angle(atoms[6], atoms[2], atoms[1], cell=[15.0, 15.0, 15.0]))
        HB_cov_dists.append(HB1_cov_dist if clv < 0 else HB1_dist)
        HB_dists.append(HB1_dist if clv < 0 else HB1_cov_dist)
        clvs.append(clv2)
        HB2_cov_dist = atoms[7].distance(atoms[5], cell=[15.0, 15.0, 15.0])
        HB2_dist = atoms[5].distance(atoms[4], cell=[15.0, 15.0, 15.0])
        HB_cov_dists.append(HB2_cov_dist if clv2 < 0 else HB2_dist)
        HB_dists.append(HB2_dist if clv2 < 0 else HB2_cov_dist)
        HB_angles.append(Atom.angle(atoms[7], atoms[5], atoms[4], cell=[15.0, 15.0, 15.0]))

for ind, step in enumerate(traj5.steps):
    if ind in tj2_HB1_and_HB2:
        atoms = step.atoms
        clv = (atoms[8].distance(atoms[10], cell=[15.0, 15.0, 15.0])-atoms[8].distance(atoms[9], cell=[15.0, 15.0, 15.0]))/2
        clv2 = (atoms[12].distance(atoms[3], cell=[15.0, 15.0, 15.0])-atoms[3].distance(atoms[4], cell=[15.0, 15.0, 15.0]))/2
        clvs.append(clv)
        HB1_cov_dist = atoms[3].distance(atoms[4], cell=[15.0, 15.0, 15.0])
        HB1_dist = atoms[3].distance(atoms[12], cell=[15.0, 15.0, 15.0])
        HB_cov_dists.append(HB1_cov_dist if clv < 0 else HB1_dist)
        HB_dists.append(HB1_dist if clv < 0 else HB1_cov_dist)
        HB_angles.append(Atom.angle(atoms[4], atoms[3], atoms[12], cell=[15.0, 15.0, 15.0]))
        clvs.append(clv2)
        HB2_cov_dist = atoms[8].distance(atoms[9], cell=[15.0, 15.0, 15.0])
        HB2_dist = atoms[8].distance(atoms[10], cell=[15.0, 15.0, 15.0])
        HB_cov_dists.append(HB2_cov_dist if clv2<0 else HB2_dist)
        HB_dists.append(HB2_dist if clv2<0 else HB2_cov_dist)
        HB_angles.append(Atom.angle(atoms[9], atoms[8], atoms[10], cell=[15.0, 15.0, 15.0]))

print(f"Mean cov dist: {mean(HB_cov_dists)}")
print(f"СКО {stdev(HB_cov_dists)}")
print(f"Mean dist: {mean(HB_dists)}")
print(f"СКО {stdev(HB_dists)}")
print(f"Mean angle: {mean(HB_angles)}")
print(f"СКО {stdev(HB_angles)}")

#plt.figure(figsize=(10, 6))
#plt.xlabel("Длина ковалентной связи, Å", fontsize=18)
#plt.ylabel("Плотность состояний", fontsize=18)
#plt.xlabel("Угол водородной связи, °", fontsize=18)
#plt.ylabel("Плотность состояний", fontsize=18)
#plt.xticks(fontsize=18)
#plt.yticks(fontsize=18)
#plt.xlim(0.9, 1.3)
#sns.kdeplot(HB_dists, fill=True, bw_adjust=1.5, color="green")
#sns.despine()

#plt.show()


ft = time.time()
print(ft-st)
