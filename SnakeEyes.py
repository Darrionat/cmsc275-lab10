# -*- coding: utf-8 -*-
"""
Created on Thu May  9 14:45:55 2019

@author: Kerri-Ann Norton
"""

import random


# Figure 16.1
def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


def checkPascal(numTrials, numRolls):
    """Assumes numTrials an int > 0
       Prints an estimate of the probability of winning"""
    numWins = 0
    for i in range(numTrials):
        for j in range(numRolls):
            d1 = rollDie()
            d2 = rollDie()
            if d1 == 1 and d2 == 1:
                numWins += 1
                break
    print('Probability of winning =', numWins / numTrials)


# checkPascal(100, 24)
# checkPascal(100000, 24)
checkPascal(10000, 10)
