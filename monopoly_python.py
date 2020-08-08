# simple text based monopoly

import math
import time
import cmath
from random import *

# Variables and Booleans
game_running = True
global overage
overage = 0
global user_position
user_position = 0

# Dictionarys and Stored Game Data
properties = dict = {1: "Vine Street", 3: "Coventry Street", 6: "Cester Square", 8: "Bow Street", 9: "Chapel Road",
                     11: "Angel Island", 13: "Trafalgar Square", 14: "North Avenue", 16: "Rough Street", 18: "Fleet Street",
                     19: "Old Kent Road", 21: "Whitehall", 23: "Penton Road", 24: "Pall Mall", 26: "Bond Street", 27: "Strand", 29: "Regent Street",
                     31: "East Road", 32: "Piccadilly", 34: "Oxford Street", 37: "Park Lane", 39: "Mayfair"}

names = dict = {1: "PlayerOne", 2: "PlayerTwo", 3: "PlayerThree",
                4: "PlayerFour", 5: "PlayerFive", 6: "PlayerSix"}
# Functions


def GameOptions():  # prints the game options easier and is established as a function
    print("1: Roll Dice")
    print("2: Edit Owned Properties")
    print("3: Make Trade")
    print("4: Help")
    print("5: End Move")


def EndMove():  # acts as the ending move selection
    print("2: Edit Owned Properties")
    print("3: Make Trade")
    print("4: Help")
    print("5: End Move")

# Classes


class Monopoly:
    def __inti__(self):
        game_running = True


class Property:
    def __init__(self, name, postion, price, rent):
        self.name = name
        self.postion = postion
        self.price = price
        self.rent = rent

    def add_smallhouse(self):
        select_newprop = input()

    def add_bighotel(self):
        select_property = input(
            "Please type carefully which property you would like to place a red hotel")


class Player:
    def __init__(self):
        self.money = 1500
        self.ownership = {}
        self.cards = {}

    def add_prop(self, prop, price):
        self.prop = prop
        self.price = price


def roll_dice():
    dice_one = randint(1, 6)
    dice_two = randint(1, 6)
    total = dice_one + dice_two
    user_position = total + overage
    overage = user_position


print("Welcome to Monopoly")
game = Monopoly()
start = input("would you like to play the game? (YES or NO)")
if start == "YES" or "yes":
    Player_One = Player()
while game_running == True:
    roll_dice()
    for p in properties:
        if user_position == p:
            print(properties[p])
