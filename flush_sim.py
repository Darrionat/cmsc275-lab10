import random


def is_flush(card_suits):
    suit = card_suits[0]
    for x in card_suits:
        if x != suit:
            return False
    return True


def sim(trials):
    suit_one = [0] * 13
    suit_two = [1] * 13
    suit_three = [2] * 13
    suit_four = [3] * 13
    deck = []
    deck.extend(suit_one)
    deck.extend(suit_two)
    deck.extend(suit_three)
    deck.extend(suit_four)
    flushes = 0
    for t in range(trials):
        hand = random.sample(deck, 5)
        if is_flush(hand):
            flushes += 1
    print(flushes / trials)


sim(100000)
