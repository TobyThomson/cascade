# Cascade - A 3D water display
Cascade is a 3D water droplet display inspired by the work of Unit 9 and their "rain rig" with a focus on creating a similar effect without the need for a camera. This repository contains all the components of cascade's design and any assoiated tools. Notes on the development process can be found at tobythomson.co.uk.

## Repository Components
1. visualizer/: The source code for a belnder plugin which visualizes the effect of the display. Used to inform cascade's mechanical requirements and generate the intial "graphics"
2. design-calcs/: Design calculations performed in Octave to establish the design requirments for the system and their implications

## Notes
* I've found Blender addon dev to be a bit of a pain. Docuentation is all over the place wiht some of it outdated and some of the avalible features just not revealed anywhere except in forum posts. I also needed to create a symlink to this directory for easy addon reloading (cmd: ln -s [THIS DIRECTORY PATH]/cascade/belnder-plugin/ /home/[USER]/.config/blender/3.0/scripts/addons/cascade-vizualiser)
