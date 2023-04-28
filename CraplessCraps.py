# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:12:02 2019

@author: Kerri-Ann Norton and modified by Darrion Thornburgh
"""
import random


def rollDie():
    return random.choice([1, 2, 3, 4, 5, 6])


def rollDie2():
    return random.choice([1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6])


def rollDie3():
    return random.choice([7, 7, 1, 7])


class CraplessCrapsGame(object):
    def __init__(self):
        self.passWins, self.passLosses = 0, 0

    def playHand(self):
        throw = rollDie3() + rollDie3()
        if throw == 7:
            self.passWins += 1
        else:
            point = throw
            while True:
                throw = rollDie3() + rollDie3()
                if throw == point:
                    self.passWins += 1
                    break
                elif throw == 7:
                    self.passLosses += 1
                    break

    def results(self):
        return (self.passWins, self.passLosses)


def variance(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    mean = sum(X) / len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    return tot / len(X)


def stdDev(X):
    """Assumes that X is a list of numbers.
       Returns the standard deviation of X"""
    return variance(X) ** 0.5


def craplessCrapsSim(handsPerGame, numGames):
    """Assumes handsPerGame and numGames are ints > 0
       Play numGames games of handsPerGame hands; print results"""
    games = []

    # Play numGames games
    for t in range(numGames):
        c = CraplessCrapsGame()
        for i in range(handsPerGame):
            c.playHand()
        games.append(c)

    # Produce statistics for each game
    pROIPerGame = []
    for g in games:
        wins, losses = g.results()
        pROIPerGame.append((wins - losses) / float(handsPerGame))

    # Produce and print summary statistics
    meanROI = str(round((100 * sum(pROIPerGame) / numGames), 4)) + '%'
    sigma = str(round(100 * stdDev(pROIPerGame), 4)) + '%'
    print('Pass:', 'Mean ROI =', meanROI, 'Std. Dev. =', sigma)


craplessCrapsSim(1000, 10)
