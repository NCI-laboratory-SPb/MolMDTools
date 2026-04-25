from xyz_trajectory import XYZ_Trajectory

file = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\DAD_ADA_Conformers.finalensemble.xyz"
file1 = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\DAD_ADA_Conformers0.finalensemble.xyz"
file2 = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\DAD_ADA_Conformers1.finalensemble.xyz"

tj = XYZ_Trajectory.xyz_traj_extr_from_xyz(file)
tj1 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file1)
tj2 = XYZ_Trajectory.xyz_traj_extr_from_xyz(file2)
tj_sum = tj.sum_traj([tj1, tj2])
print(len(tj.steps))
print(len(tj1.steps))
print(len(tj2.steps))
print(len(tj_sum.steps))

tj_sum.save(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\DAD_ADA_Conformers_sum.finalensemble.xyz")