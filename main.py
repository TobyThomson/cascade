import csv
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Control Variables
Nozzle_Grid_Width_mm = 120
Nozzle_Grid_Depth_mm = 80
Nozzle_Grid_Height_mm = 100

Nozzel_Grid_Width_Spacing = 10
Nozzel_Grid_Depth_Spacing = 8

Max_Droplets_Per_Stream = 5

CSV_File_Start_Line = 6

FPS = 5

# Create nozzle grid matricies
nozzle_grid_x_vector = np.arange(0, Nozzle_Grid_Width_mm, Nozzel_Grid_Width_Spacing)
nozzle_grid_y_vector = np.arange(0, Nozzle_Grid_Depth_mm, Nozzel_Grid_Depth_Spacing)

nozzle_grid_x_cords, nozzle_grid_y_cords = np.meshgrid(nozzle_grid_x_vector, nozzle_grid_y_vector)
nozzle_grid_z_cords =  np.full(nozzle_grid_x_cords.shape, Nozzle_Grid_Height_mm)

# Plotting setup
figure = plt.figure()
axes = figure.add_subplot(projection='3d')
droplet_lines = []

#Main
frame_interval = int((1 / FPS) * 1000)

def read_frames():
    droplet_data = []

    with open('example.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        line_number = 1
        previous_frame_index = 0
        frame = []

        print('\n*** PARSING CSV FILE ***\n')

        for row in csv_reader:
            if line_number >= CSV_File_Start_Line:
                try:
                    frame_index = int(row[0])
                    i = int(row[1])
                    j = int(row[2])
                    start = int(row[3])
                    stop = int(row[4])
                
                except:
                    print(f'\nERROR: Frame incorrectly specified in CSV file (line number {line_number})')
                    return 0
                
                if (i < 0 or i > nozzle_grid_x_cords.shape[0]) or (j < 0 or j > nozzle_grid_x_cords.shape[1]):
                    print(f'\nERROR: Specified nozzle does not exist (line number {line_number})')
                    return 0
                
                if (start > Nozzle_Grid_Height_mm or stop > Nozzle_Grid_Height_mm) or (start < 0 or stop < 0):
                    print(f'\nERROR: Specified droplet is outside canvas volume (line number {line_number})')
                    return 0

                if frame_index != previous_frame_index:
                    if (frame_index - previous_frame_index) == 1:
                        previous_frame_index = frame_index
                        droplet_data.append(frame)
                        frame = []
                        print('\n--- NEW FRAME ---\n')
                    
                    else:
                        print(f'\nERROR: Frame incorrectly indexed in CSV file (line number {line_number})')
                        return 0
                
                frame.append([i, j, start, stop])

                print(f'Frame: {frame_index} | i: {i}, j: {j}, start: {start}, stop: {stop}')
            
            line_number += 1
        
        droplet_data.append(frame)
    
    return droplet_data       

def init_canvas():
    print('\n*** SETTING UP FIGURE ***\n')

    axes.grid(False)

    axes.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    axes.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    axes.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))

    axes.set_xlabel('X (mm)')
    axes.set_ylabel('Y (mm)')
    axes.set_zlabel('Z (mm)')

    axes.set_xlim(0, Nozzle_Grid_Width_mm)
    axes.set_ylim(0, Nozzle_Grid_Depth_mm)
    axes.set_zlim(0, Nozzle_Grid_Height_mm)

    axes.view_init(20, -120)

    axes.plot_wireframe(nozzle_grid_x_cords, nozzle_grid_y_cords, nozzle_grid_z_cords, colors='grey')

def draw_frame(droplet_data):
    for droplet_line in droplet_lines:
        droplet_line[0].remove()
        del droplet_line
    
    droplet_lines[:] = []

    for droplet in droplet_data:
        droplet_x_vector = np.array([droplet[0], droplet[0]]) * Nozzel_Grid_Width_Spacing
        droplet_y_vector = np.array([droplet[1], droplet[1]]) * Nozzel_Grid_Depth_Spacing
        droplet_z_vector = np.array([droplet[2], droplet[3]])

        droplet_line = axes.plot(droplet_x_vector, droplet_y_vector, droplet_z_vector, 'blue')

        droplet_lines.append(droplet_line)

init_canvas()
droplet_data = read_frames()

if not droplet_data:
    quit()

print('\n*** BEGINING ANIMATION... ***\n')

animation = FuncAnimation(figure, draw_frame, frames=droplet_data, interval=frame_interval, repeat=True)

plt.show()