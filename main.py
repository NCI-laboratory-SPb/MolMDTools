from xyz_trajectory import XYZ_Trajectory

path = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\ADD_DAA\MTD"
file0 = "ADD-DAA-pos-1.xyz"
file1 = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\ADD_DAA\ADD-DAA-pos-1.xyz"
tj0 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=path + "\\" + file0)
tj1 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file_name=file1)
tjs = [tj1]
tj_sum = tj0.sum_traj(tjs)
print(len(tj_sum.steps))

tj_sum.save(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\ADD_DAA\ADD_DAA_closed_dimers_MTD_AIMD_sum.xyz")