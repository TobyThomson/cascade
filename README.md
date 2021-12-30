# Cascade - A 3D water display

## Steps
1. Plot nozzle grid [x]
2. Be able to read a CSV [x]
3. Plot a "frame" [x]
4. Animate "frames" based on display properties [x]
5. Check that none of the frames contain invalid is and js [x]
6. Pretty up the plot [x]
7. Read grid properties from the csv file []
8. Write tkinter CSV file selector stuff []
9. Write example program(s) which produce cool CSV files []
10. Add animation save feature []

## Improved solution:
* Use Blender to generate all the CSV files. Advantages, can do the more complex visual design here easier + all the planned python stuff.
* Use raycasting in blender to bring the 3D stuff into the rain model.
* Still have a seperate program that can read the CSV files from other programs if people want to work in those (the same CSVs will be used as the software, hardware interchange also)

## Notes
* Blender addon dev seems a bit dumb. Needed to create a symlink to this directory for easy addon reloading (cmd: ln -s /home/toby/Projects/cascade/rainman/ /home/toby/.config/blender/3.0/scripts/addons/rainman)
* Bounding box working!
* Delete overide not working in some editors.
* All previous droplet generation code implemented and working!