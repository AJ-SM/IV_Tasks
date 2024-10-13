# MiniGrid Basic Application

The project shows the implementation of the various kind of Reinfocement Learning Algorithms
By using OpenAI Gym Environment of MiniGrid(6x6).

![Grid](https://minigrid.farama.org/_images/EmptyEnv.gif)

# Table Of Contents
- [Overview](#Overview)
-  [Requirements](#Requirements)
-  [Installation](#Installation)
-  [Working](#Working)
   - [Monte Carlo](#Monte_Carlo)
   - [Q Learning](Q_Learning)
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
- Utilizing the given Reinfrocement Learning, the agent will be able to guide it's way through it. 

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

- #**Monte_Carlo** : Monte Carlo methods are ways of solving the reinforcement learning problem based on averaging sample returns. To ensure that well-defined returns are available, here we define Monte Carlo methods only for episodic tasks.

  
  
- ![Monte-Calro](https://github.com/user-attachments/assets/603fdba1-10e8-4d3c-a970-c11cad6f7f1a)






- #Q_Learnings : Q-learning is a model-free reinforcement learning algorithm used to find the optimal action-selection policy in a given environment. It works by learning a quality function (Q-value) that estimates the expected future rewards for an agent taking an action in a particular state, and then following the best policy based on these learned values.

  
![Q_learnings](https://github.com/user-attachments/assets/2946626c-9287-4ff7-9e18-9612318141ac)



- #SARSA : SARSA (State-Action-Reward-State-Action) is an on-policy reinforcement learning algorithm used to learn the optimal policy for a given environment by updating a value function based on the action taken and the resulting state-action pair.



 ![Screenshot 2024-10-13 212957](https://github.com/user-attachments/assets/85c23475-8cd4-4f3f-9815-86e7f434e05e)
 



- #SARSA_(λ) : SARSA(λ) is an extension of the SARSA algorithm that incorporates eligibility traces, allowing it to learn from multiple time steps of experience at once. This combination of SARSA and eligibility traces enables faster learning and more efficient use of past experiences compared to the standard SARSA.


![Sarsa(lambda)](https://github.com/user-attachments/assets/9b1b7c11-82e6-4a4a-bc81-f6ceb0a92370)




# Graphs_Output
The output Graphs Are As Folows: 
- **Monte Carlo** :

  
![Grid_Result](https://github.com/user-attachments/assets/ce46e792-3d31-4981-8736-724ad59d49ae)



![Gride_stepos](https://github.com/user-attachments/assets/b4fac024-a033-48b7-9b28-68aed377f3c7)


  
- Q-Learning :



![rewardepisodeQlearning](https://github.com/user-attachments/assets/0bc2e8ae-6a56-4e0f-868a-7d58383c14b6)




![Qlearning_epsvsrw](https://github.com/user-attachments/assets/8d26f46e-3ef1-47e0-a4b8-2dab733a822a)




  
- SARSA :




![Screenshot 2024-08-29 135911](https://github.com/user-attachments/assets/265fb1a4-de36-441e-882a-672be254ba03)



![Screenshot 2024-08-29 135859](https://github.com/user-attachments/assets/977cc9b9-521a-45f8-8a69-1ca527159f66)



  
- SARSA (λ) : 

![Sarsa_lambdas](https://github.com/user-attachments/assets/9d42bdb8-7f71-4907-b9fc-026fc38c2005)



![Sarsa_Lambda](https://github.com/user-attachments/assets/4d231748-8109-456e-b674-0700d35169d3)









