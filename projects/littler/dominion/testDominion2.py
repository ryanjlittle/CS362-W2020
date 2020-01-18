# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:42:42 2015

@author: tfleck
"""

from projects.littler.dominion import Dominion
from projects.littler.dominion.testUtility import *
import random
from collections import defaultdict

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]

num_players = len(player_names)

# Get the supply
supply_order = GetSupplyOrder()
supply = GetSupply(num_players)

# initialize the trash
trash = []

# Costruct the Player objects
players = GetPlayers(player_names)

# Add a bug by adding 10 cards that do nothing to the supply
supply["Buggy Card"] = [Dominion.Action_card("Buggy Card", 0, 0, 0, 0, 0)]*10

# Play the game
turn = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print(value)
        for stack in supply_order[value]:
            if stack in supply:
                print(stack, len(supply[stack]))
    print("\r")
    for player in players:
        print(player.name, player.calcpoints())
    print("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players, supply, trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)