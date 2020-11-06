'''
 * User: Hojun Lim
 * Date: 2020-11-06
'''

import sys
import math
import collections
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def fight(deck_p1: collections.deque, deck_p2: collections.deque, war_pile_p1:list = [], war_pile_p2:list = []):
    """
    deck_p1: current deck of player 1
    war_pile_p1: list of face down cards of player 1 in a war
    """

    global card_list

    cardp_1 = deck_p1.popleft()
    cardp_2 = deck_p2.popleft()

    war_pile_p1.append(cardp_1)
    war_pile_p2.append(cardp_2)

    ascii_cardp_1, ascii_cardp_2 = card_list.index(cardp_1), card_list.index(cardp_2)

    if ascii_cardp_1 > ascii_cardp_2: # player 1 wins the fight
        war_pile_p1.extend(war_pile_p2)
        for card in war_pile_p1:
            deck_p1.append(card)
        return

    elif ascii_cardp_1 < ascii_cardp_2: # player 2 wins the fight
        war_pile_p1.extend(war_pile_p2)
        for card in war_pile_p1:
            deck_p2.append(card)
        return

    else: # draw (war)
        war(deck_p1, deck_p2, war_pile_p1, war_pile_p2)


def war(deck_p1: collections.deque, deck_p2: collections.deque,  war_pile_p1:list, war_pile_p2:list):

    for i in range(3): # place three next cards
        try:
            war_pile_p1.append(deck_p1.popleft())
            war_pile_p2.append(deck_p2.popleft())

        except: # when there is no card to draw in the middle of war
            print("PAT")
            sys.exit(0)

    fight(deck_p1, deck_p2, war_pile_p1, war_pile_p2)

def begin_game(deck_p1: collections.deque, deck_p2: collections.deque):
    num_round = 0

    while deck_p1.__len__() != 0 and deck_p2.__len__() != 0:
        num_round += 1
        fight(deck_p1, deck_p2, [], [])

    print('2', num_round) if deck_p1.__len__() == 0 else print('1', num_round)


# main
deck_p1, deck_p2 = collections.deque(), collections.deque()
card_list = ['2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K', 'A'] # ordered by values (increasing, from weekest to strongest)

n = int(input())  # the number of cards for player 1

for i in range(n):
    cardp_1 = input()[:-1]
    deck_p1.append(cardp_1) # the n cards of player 1
m = int(input())  # the number of cards for player 2

for i in range(m):
    cardp_2 = input()[:-1]
    deck_p2.append(cardp_2) # the m cards of player 2


begin_game(deck_p1, deck_p2)

