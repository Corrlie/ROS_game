# ROS_game

This project is based on a popular party game - hunt the thimble. The project uses Robot Operating System (ROS) and OpenCV library and is written in Python programming language.

OS: Linux Ubuntu 20.04.1 LTS on Oracle VM VirtualBox

ROS distro: ROS Noetic

Libraries and ROS packages used:

- numpy, 
- OpenCV, 
- ROS turtlesim package - nodes: turtlesim_node and teleop_turtle_key

## Description:

First player has choose a point on the black plane (be careful not to show it to the other player!) and the other player has to find it using turtle from turtlesim package using teleoperation as soon as possible (**time is measured**). Current "temperature states" are being shown while playing the game (4 states - REALLY COLD!, cold, warm, HOT).

First player has to "hide" his point on the black window created with numpy 512x512 array. The code uses OpenCV mouse callback to get the point's position. First player can show selected point (and its x and y position) by choosing 'p' button (eng. "print") on the keyboard (but he has to be careful that the other player does not see it). He can then hide it from other player by clicking "c" (eng. "clear") on the keyboard. If the player wants to choose another point he can do this, because only the last point will be possibly saved. 
The process of choosing the point is shown below (after clicking 'p'):

![image](https://user-images.githubusercontent.com/63510085/116985636-0eb5ca00-accd-11eb-8a07-c6b52b00339a.png)

To save the point, that the other player has to seek, first player has to click "s" (eng. "saved"). After clicking "s" it is the other player turn to play. 

Second player has to find the point using turtle from turtlesim package using teleoperation. Turtlesim_node and teleop_turtle_key nodes are started automatically.

The process of finding the point using turtle is shown below:

![image](https://user-images.githubusercontent.com/63510085/116985887-5fc5be00-accd-11eb-9ae8-b7bd0e39f9cf.png)

The player has to use current "temperature" state to find the point (**the closer to the goal point - the "warmer" it is**).
After finding the point the time is shown. 

Prompts shown in the terminal are shown below:

![image](https://user-images.githubusercontent.com/63510085/116985988-8552c780-accd-11eb-8c99-81fca59632bf.png)


**IMPORTANT** - it is required to select the terminal window, not the turtle's blue window while teleoperating!

## Testing the game:

To run the game it is neccessary to have ROS Workspace catkin. In that workspace create a new package with rospy dependency and rebuild the workspace. Then download project .py files and place them in the src file of created package. After that the game is almost ready! All you have to do is run "**roscore**" command in new terminal and then in another new terminal opened in src directory (where all .py files are stored) run command "**python3 ros_game.py**". 

**That's all! Now you can play hunt the thimble using ROS!**
