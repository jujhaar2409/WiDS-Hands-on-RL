import numpy as np 
import matplotlib.pyplot as plt 

class bandit_arm:
    """
    Creates an arm which is a part of a bandit instance.
    """
    def __init__(self,arm_mean):
        self.arm_mean = arm_mean 

    def pull(self):
        return np.random.binomial(1,self.arm_mean)
    

class bandit:
    """
    Creates a (Bernoulli) bandit instance, which is fully specified by a list of arm means. 
    Functions:
        - pull(index) pulls the arm referred to by the index 
        - regret() provides the incurred regret on the bandit instance 

    NOTE: You cannot use the list of probabilities while running your algorithm! That is the whole point -- to determine those probabilities by interacting with the bandit instance again and again "efficiently".
    """
    def __init__(self,list_of_means):
        self.arms = [bandit_arm(prob) for prob in list_of_means]
        self.max_mean = max(list_of_means)
        self.regret = 0.0 
        self.count = 0 
        self.avg_reward = 0.0

    def pull(self,index):
        reward = self.arms[index].pull()
        self.regret = self.regret + (self.max_mean - reward)
        self.count += 1 
        if(self.count > 1):
            self.avg_reward = (self.avg_reward*(self.count - 1) + reward)/(self.count)
        elif(self.count == 1):
            self.avg_reward = reward
        return reward 

    def regret(self):
        return self.regret 
    
    def avg_reward(self):
        return self.avg_reward
