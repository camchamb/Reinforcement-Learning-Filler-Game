# Reinforcement-Learning-On-Filler-Game
This project is focused on creating an AI that plays the Filler game using Reinforcement Learning (RL) techniques. The goal of the Filler game is for the player to control all the colored squares on a grid by strategically expanding their territory.

# Game Overview
Filler is a grid-based puzzle game where two players control squares of changing colors. The objective is to control the majority grid vs your opponent. The game is turn-based, and at each turn, the player can expand their territory by adding adjacent same-colored squares.

# Project Overview
This repository contains the implementation of the Filler game in the Filler_Game file and the training of an Actor-Critic RL agent that learns to play the game. The agent learns optimal strategies to complete the game in the fastest time and can adjust its decisions based on the state of the environment.

You can run the game through the Python package pygame. Running the file Filler_Simulator.py will start a new game and simulation. Running the Training_RL.py will begin to train the RL model. It will print the scores obtained from each game simulation and will save the model when major improvements are made. 
