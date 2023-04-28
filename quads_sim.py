from itertools import combinations
import random


def is_cap(points):
    for comb in combinations(points, 3):
        exclude = 0
        for x in comb:
            exclude ^= x
        if exclude in points:
            return False
    return True


def sim(trials):
    deck = list(range(64))
    caps = 0
    for trial in range(trials):
        cards = random.sample(deck, 9)
        if is_cap(cards):
            caps += 1
    print(caps / trials)


sim(100000)
