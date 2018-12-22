# Skate Space

This project was created for Fresno State's CSCI 166 - Principles of Artificial Intelligence class, taught by professor David Ruby.

In this project, we explore value iteration and Q-learning inside a grid-world. The distinguishing feature of this world versus most grid worlds is that movement in a direction does not stop until the agent runs into an obstacle.

The goal of the agent is to collect the keys that are in the level and go to the exit. Doing so will win the level. The catch is that the keys can also move, so the agent must make informed decisions about when to wait and move in order to get a key.

## Developers

[Zachary Andersen](https://github.com/Xakaree)

Abhishek Gupta

[Joshua Holland](https://github.com/ggkfox)

Juan Mejia

[Mark Philipp](https://github.com/mphilipp622)

## Pre-requisites

The project can be run using Python 2.7 or Python 3+

The following modules must be installed to compile and run the program:

	- TKinter
	- pillow
	- keyboard
	
It's recommended to use pip to install the above packages.

**pip install pillow**

**pip install keyboard**

**pip install tkinter**

NOTE: Python 2 uses a capital T for Tkinter. Python 3 is all lowercase: tkinter

## How to run

Open a python terminal and navigate to the root directory of the repository.

### Running Value Iteration
Now, to run value iteration, put in the following syntax:

python main.py &lt;*nameOfJsonFile*>.json v &lt;*rewardDiscount*> &lt;*livingReward*> &lt;*iterations*> 

E.G: **python main.py level1.json v 0.8 1 25**

**nameOfJsonFile**  = the name of the file that contains the level JSON data.

**rewardDiscount** 	= how much weight the agent gives to future rewards vs. immediate rewards. A high value (e.g 0.8) will favor later rewards while a low value (e.g 0.2) will favor immediate rewards.

**livingReward**	= Specifies how much of a reward is given to the agent for being alive. This value is always added to the total reward of an action that is taken. For instance, to reward the agent for staying alive, you can set this value to a positive. To punish it for staying alive, you can give it a negative value. This will ideally force the agent to try and finish more quickly.

**iterations**		= This is the number of iterations the algorithm runs to find a policy to use. The higher iterations, the more accurate the policy. However, a large iterations value will take much longer to computer. Lower iterations compile quickly, but may not result in an optimal policy.

###	Running Q-Learning

python main.py &lt;*nameOfJsonFile*>.json q &lt;*rewardDiscount*> &lt;*livingReward*> &lt;*learningRate*> &lt;*epsilon*>

E.G: **python main.py level1.json q 0.5 -1 0.2 0.9**

**rewardDiscount, livingReward, and nameOfJsonFile** are described in the value iteration section, above.

**learningRate**	= This is a value between 0 and 1 that specifies how much the agent weighs newly found data versus old data. For instance, if learningRate is high (0.8), then the new reward found from the action just taken will weigh heavier than the old value the agent had previously found from taking that action. In contrast, a lower value (0.2), will weight previous values more.

**epsilon**			= This is a value between 0 and 1 that dictates a probability the agent takes a random action that is off-policy. Note that the epsilon value decays exponentially with each game that's played by the agent. The idea is to encourage the agent to explore options that are off-policy with some small chance. A high epsilon means the agent will take a lot of random actions early on, which will decay over time. A low value means the agent will be less likely to take random actions.

## Value Iteration Compilation Time

Value iteration takes a relatively long time to compute, especially for large levels. You might have to be patient while waiting for the program to start running.

## Modifying the AI Variables

For value iteration, you can modify the number of iterations, the reward discount, and the living reward in the **mdp.py** file in the MDP class constructor.

```python
 def __init__ (self, startingState, iterations = None):
        # Variables that change the AI behavior
        self.rewardDiscount = 0.5
        self.livingReward = 0
        self.iterations = iterations if iterations != None else 10
```

For Q-Learning, you can modify Epsilon, reward discount, living reward, and learning rate by going to the **qLearning.py** file and changing the values in the QLearn class constructor.

```python
def __init__(self, startingState):
		# Variables that change the AI behavior
		self.rewardDiscount = 0.5
		self.livingReward = -1
		self.learningRate = 0.2
		self.epsilon = 0.9
```

## Creating Levels

Level parsing is handled using JSON. If you want to create your own levels, refer to some of the existing JSON files in the root directory. Once you create a level, you can simply load it using the command line argument when you run the program, as outlined in the "How to run" section, above.