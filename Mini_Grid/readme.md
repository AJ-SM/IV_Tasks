# MiniGrid Basic Application

The project shows the implementation of the various kind of Reinfocement Learning Algorithms
By using OpenAI Gym Environment of MiniGrid(6x6).

# Table Of Contents
- [Overview](#Overview)
-  [Requirements](#Requirements)
-  [Installation](#Installation)
-  [Working](#Working)
   - [Monte Carlo](#Monte_Carlo)
   -[Q Learning](Q_Learning)
   - [SARSA](#SARSA) 
   - [SARSA(λ)](#SARSA_(λ))
-  [Graphs_Output](#Graphs_Output)


# Overview
The Minigird 6x6 will we be used to implement the reinforcement Learning :
- Monte Carlo Learning
- Q Learning
- SARSA (State -> Action ->  Reward -> State -> Action)
- SARSA (λ)

# Agents Workflow
- The agent start from at the bottom-right corner of the Grid
- The goal is the agent have to reach to Bottom-right corener.

# Requirements
- Python 3.x (or Greater)
- [OpenAi Gym]([https://gymnasium.farama.org/])
- [Minigrid]([https://github.com/MAN1986/pyamaze/blob/main/pyamaze/pyamaze.py](https://minigrid.farama.org/environments/minigrid/EmptyEnv/))

# Installation 
- Install OpenAi Gym
  ``` bash
  git clone https://github.com/openai/gym 
-  Clone the Repository:
   ``` bash  
     git clone https://github.com/AJ-SM/IV_Tasks/tree/main/Mini_Grid)](https://github.com/AJ-SM/IV_Tasks/tree/main/Mini_Grid

# Working
- **DSF** : The DFS algorithm function to solve the maze. It navigates through the maze by checking possible movements in the East, South, North, and West directions. It traces the solution path from the goal back to the start.
-** Mv_east(p), M_west(p), M_north(p), M_south(p):** Helper functions that define movements in the maze based on the direction.
- **maze.tracePath():** Visualizes the path taken by the agent to solve the maze.

# Monte_Carlo

# Q_Learning 

# SARSA 

# SARSA_(λ)




# Graphs_Output
The output Graphs Are As Folows: 
- **Monte Carlo**
  
- **Q-Learning**
  
- **SARSA**
  
- **SARSA (λ)**










