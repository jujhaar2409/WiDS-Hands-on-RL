# Part 2

We will wrap up dynamic programming in this part and dig into the core ideas of RL, starting with the prediction and control problems. Then we will investigate a simple control algorithm and finally move towards Monte Carlo prediction and control methods.

## Lecture 10: Policy Iteration from [CS747](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2022/index.html)

There are two dynamic programming methods widely used to evaluate policies in MDPs. The first is value iteration, which we covered towards the end of last week and the other one if policy iteration.

The final method for policy evaluation on MDPs is Linear Programming. If you are interested, you can have a look at this from lecture 9 of CS747. This is an optional topic.

## Lecture 13: Prediction & Control, Basic Model-based Control from [CS747](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2022/index.html)

There are two major "tasks" in RL: prediction and control. Prediction involves approximating how well a particular policy performs on the MDP to gauge how good it is by calculating something like the action-value function(Q). In control, the goal is to find the optimal policy for the given MDP.

This lecture covers these two problems in the initial section and later introduces a simple and intuitive control algorithm called "model based control".

**NOTE:** Skip slides 6/16 to 9/16.

## Assignment 2: Dynamic Programming

You can find assignment 2 in [this](./assignment2/) folder. The details can be found in the [readme](./assignment2/README.md) file in the folder linked above.

Completion of this assignment is a compulsory requirement of the project.
