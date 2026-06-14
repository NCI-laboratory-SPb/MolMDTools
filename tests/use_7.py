import time

from molmdtools.xyz_trajectory import XYZ_Trajectory
from molmdtools.hydrogen_bond import Hydrogen_Bond
from molmdtools.files_translator import Files_Translator

st = time.time()

Files_Translator.dump2xyz(filename="file_start.dump", final_filename="file_final.xyz")

file_name = "file.xyz"
traj = XYZ_Trajectory.extr_from_xyz(file_name=file_name)

print(len(traj.steps))

HB1_cov_dist = traj.dist_list(10, 4)
HB2_cov_dist = traj.dist_list(11, 7)
HB1_noncov_dist = traj.dist_list(13, 4)
HB2_noncov_dist = traj.dist_list(12, 7)
HB1_angle = traj.angle_list(10, 4, 13)
HB2_angle = traj.angle_list(11, 7, 12)
HB1_tors_ang = traj.torsion_angle_list(11, 1, 13, 4)
HB2_tors_ang = traj.torsion_angle_list(10, 0, 12, 7)


HB1_clvs1 = []
HB2_clvs1 = []

for step in traj.steps:
    atoms = step.atoms
    HB1_clvs1.append(Hydrogen_Bond([atoms[10], atoms[4], atoms[13]]).colvar)
    HB2_clvs1.append(Hydrogen_Bond([atoms[11], atoms[7], atoms[12]]).colvar)

assert len(HB1_cov_dist) == len(HB2_cov_dist) == len(HB1_noncov_dist) == len(HB2_noncov_dist) == len(HB1_angle) == len(HB2_angle) == len(HB1_tors_ang) == len(HB2_tors_ang) == len(HB1_clvs1) == len(HB2_clvs1)

len_data = len(HB1_angle)
print(len_data)

data = iter(["".join([str(i), str(round(HB1_cov_dist[i], 2)).rjust(10), str(round(HB2_cov_dist[i], 2)).rjust(10),
                 str(round(HB1_noncov_dist[i], 2)).rjust(10), str(round(HB2_noncov_dist[i], 2)).rjust(10),
                 str(round(HB1_angle[i], 2)).rjust(10), str(round(HB2_angle[i], 2)).rjust(10),
                 str(round(HB1_tors_ang[i], 2)).rjust(10), str(round(HB2_tors_ang[i], 2)).rjust(10),
                 str(round(HB1_clvs1[i], 2)).rjust(10), str(round(HB2_clvs1[i], 2)).rjust(10), "\n"]) for i in range(len_data)])

with open("amidines_5_5ns.csv", "w") as file:
    file.write("No" + "r(D, H)1" + "r(D, H)2" + "r(H, A)1" + "r(H, A)2" + "angle(D, H, A)1" + "angle(D, H, A)2" + "tors_angl(N, C, A, H)1" + "tors_angl(N, C, A, H)2" + "clv1_HB1" + "clv1_HB2" + "\n")
    for i in range(len_data):
        file.write(next(data))

ft = time.time()
print(ft-st)
