import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

# Setup
Nozzle_Grid_Width_mm = 120
Nozzle_Grid_Depth_mm = 80
Nozzle_Grid_Height_mm = 100

Nozzel_Grid_Width_Spacing = 12
Nozzel_Grid_Depth_Spacing = 8

Max_Droplets_Per_Stream = 5

# Create nozzle grid matricies
nozzle_grid_x_vector = np.linspace(0, Nozzle_Grid_Width_mm, Nozzel_Grid_Width_Spacing)
nozzle_grid_y_vector = np.linspace(0, Nozzle_Grid_Depth_mm, Nozzel_Grid_Depth_Spacing)

nozzle_grid_x_cords, nozzle_grid_y_cords = np.meshgrid(nozzle_grid_x_vector, nozzle_grid_y_vector)
nozzle_grid_z_cords =  np.full(nozzle_grid_x_cords.shape, Nozzle_Grid_Height_mm)

# Plotting setup
figure = plt.figure()
axes = figure.add_subplot(projection='3d')

# Plot nozzel grid
axes.plot_wireframe(nozzle_grid_x_cords, nozzle_grid_y_cords, nozzle_grid_z_cords)

axes.set_xlabel('X (mm)')
axes.set_ylabel('Y (mm)')
axes.set_zlabel('Z (mm)')

axes.set_xlim(0, Nozzle_Grid_Width_mm)
axes.set_ylim(0, Nozzle_Grid_Depth_mm)
axes.set_zlim(0, Nozzle_Grid_Height_mm)

axes.view_init(20, -120)

plt.show()