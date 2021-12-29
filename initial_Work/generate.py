import csv
import shutil
import numpy as np

Max_Height_mm = 100
Step_Size_mm = 1
Droplet_Size_mm = 1

Output_Filename = 'example.csv'

shutil.copyfile('header.csv', Output_Filename)

zero_frame = np.full(np.zeros([1, 12, 10]).shape, Max_Height_mm)
animation = zero_frame

def add_frame_to_animation(animation, frame):
    return np.concatenate([animation, frame])

animation = add_frame_to_animation(animation, zero_frame)

for x in range(Max_Height_mm, 0, -Step_Size_mm):
    frame = np.full(zero_frame.shape, x)
    animation = add_frame_to_animation(animation, frame)

print(animation.shape[0])

with open(Output_Filename, 'a') as csv_file:
    writer = csv.writer(csv_file)

    for frame_index in range(0, animation.shape[0]):
        for column_index in range(0, animation.shape[1]):
            for row_index in range(0, animation.shape[2]):
                start_height = animation[frame_index][column_index][row_index]
                stop_height = start_height - Droplet_Size_mm

                writer.writerow([frame_index, column_index, row_index, start_height, stop_height])

                print(f'Frame: {frame_index} | i: {column_index}, j: {row_index}, start: {start_height}, stop: {stop_height}')
