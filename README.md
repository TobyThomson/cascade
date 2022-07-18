# Cascade - A 3D Water Droplet Display
Cascade is a 3D water droplet display inspired by the work of Unit 9 and their "rain rig", with a focus on creating a similar effect without the need for a camera. This repository contains all the components of cascade's design and any associated tools. Notes on the development process can be found on [my website](https://www.tobythomson.co.uk).

## Repository Components
1. visualizer/: The source code for the blender plugin which visualizes the effect of the display. Used to inform cascade's mechanical requirements and generate the intial "graphics"
2. design-calcs/: Design calculations used to establish the design requirements for the system and their implications
3. design/: The MCAD (Mechanical CAD) and ECAD (Electrical CAD) files to assemble a display. Mechanical design created in FreeCAD. Electrical design done in KiCAD.

## Visualizer
### Notes
* I've found Blender add-on dev to be a bit of a pain. Documentation is all over the place with some of it outdated and some of the avalible features just not revealed anywhere except in forum posts. Forgive the sloppy code.
* For a clean Blender workspace that only features the bare minimum required to play with the visualizer, `visulization_setup.blend`is included.

### Installation
For Linux users, to install the visulaizer add-on:
1. Run the following command in a terminal:
`ln -s [THIS DIRECTORY FULL PATH]/visualizer/ /home/[USER]/.config/blender/3.0/scripts/add-ons/cascade_vizualiser`. This will create a symlink between between Blender's add-on directory and this directory (useful if you want to modify the add-on without having to go through the convoluted add-on reloading process in Blender)
2. Open Blender
3. Enable the add-on (`Edit > Preferences > Add-ons > Community` and check the box by `Cascade Visualizer`)
4. Profit

For Mac and Windows users (+ Linux users who don't want to modify things): idk. Probably zip up **the contents** of `visualizer/` as `cascade_visualizer.zip` and use the Blender interface to install it (`Edit > Preferences > Add-ons > Install...`)?

### Usage
Just have a play. You'll work it out. Features are limited at the time of writing. Will flesh this out when things get more complex. For inexperienced Blender users, see the comment on `visulaization_setup.blend`. Once the add-on has been installed, you can close Blender then open this file to provide a slightly stripped back Blender inteface.

### To Do
* [] Clean up code a bit
* [] Implement the "Bake CSV" and "Load CSV" fetaures
* [] Fix bug encounted whern trying to disable the addon before having used it to generate any droplets
* [x] Add a field which shows how many nozzels would be required for the given configuration
* [x] Update default parameters to something more realistic
* [x] Fix name of plugin as shown in Blender's toolbar
* [x] Remove excessive panels