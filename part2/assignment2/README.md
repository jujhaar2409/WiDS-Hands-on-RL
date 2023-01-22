# Assignment 2: Dynamic Programming

You will be implementing methods of dynamic programming in this assignment on sample MDPs. Don't be afraid to ask doubts; direct them to either mentor.

## Goal

Implement the two dynamic programming algorithms you have learnt, policy iteration and value iteration, through the content of this part to find the solution to a given MDP.

Explain your code well by adding comments.

Try comparing the two(or three if you do the bonus) methods and see which seems to be faster; think of reasons why. Write them as comments in your code or maintain a separate markdown/text document.

## Test MDPs format

You are given two MDPs to test on in the [MDPs](./MDPs) folder. Both are continuing MDPs. They follow the format:

```html
states <number of states>
actions <number of actions>
tran <initial state> <action taken> <final state> <reward> <transition probability>
...all the other transitions...
tran <initial state> <action taken> <final state> <reward> <transition probability>
gamma  <discount rate>
```

The solutions to the MDPs are contained in the same directory. You can use these solutions to verify the output of your MDP planner. The format:

```html
<optimal value function for first state> <optimal action for first state>
...one entry for each state...
<optimal value function for last state> <optimal action for last state>
```

## A Rough Outline

- The first step would be parse through the MDP files and store them into suitable data structures in python.
- Next, you have to implement the algorithms and store their results in the code.
- Finally, you can make a function that takes the results generated and stores them in an output text file so that you can verify the solution.
- You can also write another script to automate the process: run your python file and then compare the output produced to the solutions of the test MDPs provided. But, this isn't necessary as the MDPs aren't too big in size anyways.

(you can choose to go about this differently, discuss with one of the mentors if you do)

## Bonus

If you find extra time on your hands, you can try implementing linear programming, another technique to solve MDPs, as well. You can find details on linear programming for MDP planning in [Lecture 9 of CS747](https://www.cse.iitb.ac.in/~shivaram/teaching/old/cs747-a2022/lectures/cs747a2022l09.pdf).
