import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

from xyz_trajectory import XYZ_Trajectory

file = r"file.xyz"

tj = XYZ_Trajectory.extr_from_xyz(file)
tj1 = tj.subsystem_traj([0, 1, 2, 3, 4, 10, 11])
tj2 = tj.subsystem_traj([5, 6, 7, 8, 9, 12, 13])
print(len(tj1.steps))
print(len(tj2.steps))





torsion_angles_1 = tj1.torsion_angle_list(5, 0, 4, 3)
torsion_angles_2 = tj2.torsion_angle_list(3, 4, 0, 5)

plt.scatter(torsion_angles_1, torsion_angles_2, s=1)
plt.xlabel('Torsion angles of subsystem 1')
plt.ylabel('Torsion angles of subsystem 2')
plt.title('Correlation between torsion angles of two subsystems')
plt.show()





centers_of_mass_1 = tj1.center_of_mass_list()
centers_of_mass_2 = tj2.center_of_mass_list()
difference = []
for i in range(len(centers_of_mass_1)):
    x_diff = centers_of_mass_1[i][0] - centers_of_mass_2[i][0]
    y_diff = centers_of_mass_1[i][1] - centers_of_mass_2[i][1]
    z_diff = centers_of_mass_1[i][2] - centers_of_mass_2[i][2]
    difference.append((x_diff, y_diff, z_diff))

points = np.array(difference)
x, y, z = points.T
kde = gaussian_kde(points.T)
density = kde(points.T)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
scatter = ax.scatter(x, y, z, c=density)

cbar = plt.colorbar(scatter)
cbar.set_label('Density')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()





c_coords_1 = [step.atoms[0].coords for step in tj1.steps]
c_coords_2 = [step.atoms[0].coords for step in tj2.steps]
vec1 = np.array(c_coords_1) - np.array(centers_of_mass_1)
vec2 = np.array(c_coords_2) - np.array(centers_of_mass_2)
vector_product = np.cross(vec1, vec2)
vector_product_magnitudes = np.linalg.norm(vector_product, axis=1)
vector_product = vector_product/vector_product_magnitudes[:, np.newaxis]

x, y, z = vector_product.T

theta = np.arccos(z)  
phi = np.arctan2(y, x)  

plt.figure()

hb = plt.hexbin(
    phi, theta,
    gridsize=100,
    cmap='viridis'
)

plt.colorbar(hb, label="Density")

plt.xlabel("φ (azimuth)")
plt.ylabel("θ (polar)")
plt.title("Density on sphere (projection)")

plt.show()


fig = plt.figure()
ax = fig.add_subplot(projection='mollweide')

hb = ax.hexbin(
    phi, np.pi/2 - theta,  
    gridsize=100,
    cmap='viridis'
)

plt.colorbar(hb, label="Density")

ax.set_title("Spherical density (Mollweide projection)")

plt.show()
