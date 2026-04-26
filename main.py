from xyz_trajectory import XYZ_Trajectory

file = r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\ADD_DAA_Conformers_0.xyz"
files = [f"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\ADD_DAA_Conformers_{i}.xyz" for i in range(1, 30)]
tj = XYZ_Trajectory.xyz_traj_extr_from_xyz(file)
tjs = [XYZ_Trajectory.xyz_traj_extr_from_xyz(file) for file in files]

tj_sum = tj.sum_traj(tjs)
print(len(tj_sum.steps))

tj_sum.save(file_name=r"D:\SPBU\Tolstoy_Lab\Cooperativity\Three_Bonds\DAD_ADA\Conformers\ADD_DAA_Conformers_all_opt_confs.xyz")