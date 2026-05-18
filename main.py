import time
from statistics import mean, stdev

import matplotlib.pyplot as plt
import seaborn as sns

from atom import Atom
from xyz_trajectory import XYZ_Trajectory
from hydrogen_bond import HB_Analyzer

st = time.time()

traj = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Benzamidines\AIMD\E-anti_E-anti\E-anti_E-anti-pos-1.xyz")
traj1 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Benzamidines\AIMD\E-syn_Z-anti\E-syn_Z-anti-pos-1.xyz")
traj2 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Benzamidines\AIMD\Z-anti_E-syn\Z-anti_E-syn-pos-1.xyz")
traj3 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Benzamidines\AIMD\Z-anti_Z-anti\Z-anti_Z-anti-pos-1.xyz")
traj4 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Two_Bonds\Benzamidines\AIMD\Z-anti_Z-syn\Z-anti_Z-syn-pos-1.xyz")


tj1 = traj

print(len(tj1.steps))

print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[26, 2, 1])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[27, 5, 4])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[26, 5, 1])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[27, 2, 4])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[26, 5, 27])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[26, 2, 27])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[4, 2, 1])))
print(len(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[4, 5, 1])))

#tj_10_8_9_and_4_3_12 = set(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[10, 8, 9])).intersection(set(HB_Analyzer.hb_in_traj(traj=tj1, atoms_nums=[4, 3, 12])))

#clvs = []
#HB_cov_dists = []
#HB_dists = []
#HB_angles = []
#
#for ind, step in enumerate(traj.steps):
#    if ind in tj_10_8_9_and_4_3_12:
#        atoms = step.atoms
#        clv = (atoms[9].dist(atoms[8], cell=[15.0, 15.0, 15.0])-atoms[10].dist(atoms[8], cell=[15.0, 15.0, 15.0]))/2
#        clv2 = (atoms[4].dist(atoms[3], cell=[15.0, 15.0, 15.0])-atoms[12].dist(atoms[3], cell=[15.0, 15.0, 15.0]))/2
#        clvs.append(clv)
#        HB1_cov_dist = atoms[9].dist(atoms[8], cell=[15.0, 15.0, 15.0])
#        HB1_dist = atoms[8].dist(atoms[10], cell=[15.0, 15.0, 15.0])
#        HB_angles.append(Atom.angle(atoms[10], atoms[8], atoms[9], cell=[15.0, 15.0, 15.0]))
#        HB_cov_dists.append(HB1_cov_dist)
#        HB_dists.append(HB1_dist)
#        clvs.append(clv2)
#        HB2_cov_dist = atoms[4].dist(atoms[3], cell=[15.0, 15.0, 15.0])
#        HB2_dist = atoms[3].dist(atoms[12], cell=[15.0, 15.0, 15.0])
#        HB_cov_dists.append(HB2_cov_dist)
#        HB_dists.append(HB2_dist)
#        HB_angles.append(Atom.angle(atoms[4], atoms[3], atoms[12], cell=[15.0, 15.0, 15.0]))
#
#print(f"Mean cov dist: {mean(HB_cov_dists)}")
#print(f"СКО {stdev(HB_cov_dists)}")
#print(f"Mean dist: {mean(HB_dists)}")
#print(f"СКО {stdev(HB_dists)}")
#print(f"Mean angle: {mean(HB_angles)}")
#print(f"СКО {stdev(HB_angles)}")
#
#print({len([x for x in clvs if abs(x)<0.1])})

#plt.figure(figsize=(10, 6))
#plt.xlabel("Длина связи акцептор водородной связи - атом водорода, Å", fontsize=18)
#plt.ylabel("Плотность состояний", fontsize=18)
#plt.xlabel("Угол водородной связи, °", fontsize=18)
#plt.ylabel("Плотность состояний", fontsize=18)
#plt.xticks(fontsize=18)
#plt.yticks(fontsize=18)
#plt.xlim(0.9, 1.3)
#sns.kdeplot(HB_angles, fill=True, bw_adjust=1.5, color="green")
#sns.despine()
#
#plt.show()


ft = time.time()
print(ft-st)
