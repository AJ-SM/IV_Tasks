# Maze Solving using DFS with Pyamaze

The project will show the impelmentation of Deep First Seach(DFS) using **Python** and **Maze** generation library for sort of better visualization.
This can be done by using **pymaze** 


# Table Of Contents
- [Overview](#Overview)
-  [Agents Workflow](#Agents Workflow)
-  [Requirements](#Requirements)
-  [Installation](#Installation)


# Overview
The pyamaze 

https://github.com/user-attachments/assets/8e7f7e02-2598-4003-8fba-e8767ed435ad



https://github.com/user-attachments/assets/155c1931-ed2d-48a3-a3e3-faf0e4962e1f

will generates the gird of specification (for this project 10x10 has been used), and uses the DFS algorithm to get through it.

# Agents Workflow
- The agent start from at the bottom-right corner of the maze
- The goal is the agent have to reach to top-left corener while leaving a trail of footprints.

# Requirements
- Python 3.x (or Greater)
- [Pyamaze](https://github.com/MAN1986/pyamaze/blob/main/pyamaze/pyamaze.py)

# Installation 
- Install Pyamaze
  ``` bash
  git clone https://github.com/MAN1986/pyamaze/blob/main/pyamaze/pyamaze.py 
-  Clone the Repository:
   ``` bash  
     git clone
    https://github.com/AJ-SM/IV_Tasks/blob/main/DFS/new.py

# Working
- **DSF** : The DFS algorithm function to solve the maze. It navigates through the maze by checking possible movements in the East, South, North, and West directions. It traces the solution path from the goal back to the start.
-** Mv_east(p), M_west(p), M_north(p), M_south(p):** Helper functions that define movements in the maze based on the direction.
- **maze.tracePath():** Visualizes the path taken by the agent to solve the maze.

# Example Output
The agent will navigate through the maze , and the path will be traced on the graphical display. The agent is represented bya red square, and the footprints it leaves behind help visualize the progress through the maze.










