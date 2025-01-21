# This one was supposed to be tedious, so I avoided it for a while.
# The challenge with this one was just to implement it as fast as possible without making mistakes or getting bored.
# I did it in 18 minutes, approximately, and I would say about three or four were spent debugging elementary errors (parse errors, etc.)
# Claude helped type.
from enum import Enum

class HandType(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

class Card:
    def __init__(self, s):
        self.value = s[0]
        if self.value == 'T':
            self.value = 10
        elif self.value == 'J':
            self.value = 11
        elif self.value == 'Q':
            self.value = 12
        elif self.value == 'K':
            self.value = 13
        elif self.value == 'A':
            self.value = 14
        else:
            self.value = int(self.value)
        self.suit = s[1]

    def __lt__(self, other):
        return self.value < other.value

def score_hand(hand):
    ([card.value for card in hand])
    hand.sort()
    is_flush = len(set(card.suit for card in hand)) == 1
    is_straight = len(set(card.value for card in hand)) == 5 and (max(card.value for card in hand) - min(card.value for card in hand) == 4) or \
        set(card.value for card in hand) == set([2, 3, 4, 5, 14])
    
    if is_straight:
        tiebreakers = [hand[3].value] # this nicely handles the case where the ace is the lowest card
    if is_flush and is_straight:
        return HandType.STRAIGHT_FLUSH, tiebreakers
    if is_straight:
        return HandType.STRAIGHT, tiebreakers
    if is_flush:
        tiebreakers = [card.value for card in hand[-1::-1]]
        return HandType.FLUSH, tiebreakers
    
    if (hand[0].value == hand[1].value == hand[2].value == hand[3].value):
        return HandType.FOUR_OF_A_KIND, [hand[0].value, hand[4].value]
    if (hand[1].value == hand[2].value == hand[3].value == hand[4].value):
        return HandType.FOUR_OF_A_KIND, [hand[1].value, hand[0].value]
    
    if (hand[0].value == hand[1].value == hand[2].value) and (hand[3].value == hand[4].value):
        return HandType.FULL_HOUSE, [hand[0].value, hand[3].value]
    if (hand[0].value == hand[1].value) and (hand[2].value == hand[3].value == hand[4].value):
        return HandType.FULL_HOUSE, [hand[2].value, hand[0].value]
    
    if (hand[0].value == hand[1].value == hand[2].value):
        return HandType.THREE_OF_A_KIND, [hand[0].value, hand[4].value, hand[3].value]
    if (hand[1].value == hand[2].value == hand[3].value):
        return HandType.THREE_OF_A_KIND, [hand[1].value, hand[4].value, hand[0].value]
    if (hand[2].value == hand[3].value == hand[4].value):
        return HandType.THREE_OF_A_KIND, [hand[2].value, hand[1].value, hand[0].value]

    if (hand[0].value == hand[1].value) and (hand[2].value == hand[3].value):
        return HandType.TWO_PAIR, [hand[0].value, hand[2].value, hand[4].value]
    if (hand[0].value == hand[1].value) and (hand[3].value == hand[4].value):
        return HandType.TWO_PAIR, [hand[3].value, hand[0].value, hand[2].value]
    if (hand[1].value == hand[2].value) and (hand[3].value == hand[4].value):
        return HandType.TWO_PAIR, [hand[3].value, hand[1].value, hand[0].value]
    
    if (hand[0].value == hand[1].value):
        return HandType.ONE_PAIR, [hand[0].value, hand[4].value, hand[3].value, hand[2].value]
    if (hand[1].value == hand[2].value):
        return HandType.ONE_PAIR, [hand[1].value, hand[4].value, hand[3].value, hand[0].value]
    if (hand[2].value == hand[3].value):
        return HandType.ONE_PAIR, [hand[2].value, hand[4].value, hand[1].value, hand[0].value]
    if (hand[3].value == hand[4].value):
        return HandType.ONE_PAIR, [hand[3].value, hand[2].value, hand[1].value, hand[0].value]
    
    return HandType.HIGH_CARD, [card.value for card in hand[-1::-1]]

def compare_hands(hand1, hand2):
    hand1_type, hand1_tiebreakers = score_hand(hand1)
    hand2_type, hand2_tiebreakers = score_hand(hand2)
    if hand1_type.value > hand2_type.value:
        return 1
    if hand1_type.value < hand2_type.value:
        return -1
    # if we reached this point they are of the same type and we need to compare the tiebreakers
    # the tiebreakers are guaranteed to be the same length and the most important one comes first
    for i in range(len(hand1_tiebreakers)):
        if hand1_tiebreakers[i] > hand2_tiebreakers[i]:
            return 1
        if hand1_tiebreakers[i] < hand2_tiebreakers[i]:
            return -1
    return 0

p1_wins = 0
with open('54/poker.txt', 'r') as f:
    for line in f:
        hands = line.strip().split()
        if compare_hands([Card(card) for card in hands[:5]], [Card(card) for card in hands[5:]]) == 1:
            p1_wins += 1
print(p1_wins)