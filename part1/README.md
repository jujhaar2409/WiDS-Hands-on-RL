# Part 1

In this part, we will cover multi-armed bandits and markov decision processes.

## Chapter 1 of Sutton and Barto (optional reading)

This chapter provides a very nice "birds eye view" of RL and will provide context to all the things that you will be reading about. That being said, this is an optional reading.

## Chapter 2 of Sutton and Barto

This chapter deals with the notion of multi-armed bandits.

What are bandits? Imagine a slot machine with many "arms" -- typically, you pull one of these and get some reward. The problem here is figuring out which arm to pull, and the fact is that slot machines steal your money! Hence the term "bandits".

So, what is fascinating about these bandits?

**Challenge**: Can you come up with an algorithm which gives maximum *expected* reward over ALL bandit instances?

This challenge, and the connections between bandits and RL will become more and more apparent as you study this chapter.

## Chapter 3 of Sutton and Barto (upto section 3.4)

These sections will introduce you to Markov Decision Processes and their mathematical formulation. These will be a key element of our study of RL ahead.

## Lectures 6 and 8 from [CS747](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2022/index.html)

The lectures cover definitions for Policies, Value functions, Evaluation, as well as the optimality operator and will introduce you to a technique called value iteration used to find the optimal value function.

## Assignment 1: Bandit Algorithms

You can find the first programming assignment which is based on bandit algorithms [here](./assignment1). Instructions for the assignment are in the jupyter notebook linked [here](./assignment1/bandits_exercise.ipynb).

Completion of this assignment is a compulsory requirement of the project.
