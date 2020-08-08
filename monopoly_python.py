# simple text based monopoly

import math
import time 
import cmath
from random import *

# Variables and Booleans
game_running = True
#

# Dictionarys and Stored Game Data 

properties = dict = {1: "Vine Street", 3: "Coventry Street", 6: "Cester Square", 8: "Bow Street" , 9: "Chapel Road", 
11: "Angel Island", 13: "Trafalgar Square", 14: "North Avenue", 16: "Rough Street", 18: "Fleet Street", 
19: "Old Kent Road", 21: "Whitehall", 23: "Penton Road", 24: "Pall Mall", 26: "Bond Street", 27: "Strand", 29: "Regent Street",
31: "East Road", 32: "Piccadilly", 34: "Oxford Street", 37: "Park Lane", 39: "Mayfair", "Rent_Brown": 5, "Rent_LBlue": 15,
"Rent_Pink": 25, "Rent_Orange": 50, "Rent_Red": 75, "Rent_Yellow": 90, "Rent_Green": 105, "Rent_Blue": 125, "Buy_Brown": 50, "Buy_LBlue": 90, "Buy_Pink": 125,
"Buy_Orange": 150, "Buy_Red": 175, "Buy_Yellow": 200, "Buy_Green": 225, "Buy_Blue": 250}

# Functions

def GameOptions(): # prints the game options easier and is established as a function 
	print("1: Roll Dice")
	print("2: Edit Owned Properties")
	print("3: Make Trade")
	print("4: Help")
	print("5: End Move")


def EndMove(): # acts as the ending move selection
	print("2: Edit Owned Properties")
	print("3: Make Trade")
	print("4: Help")
	print("5: End Move")

#

# Classes

class Monopoly:
	def __init__(self,players):
		self.players = players
	
	def start_game(self):
		print("Welcome to Monopoly the Text Edition")

class Property:
	def __init__(self,name,postion,price,rent):
        self.name = name
        self.postion = postion
        self.price = price
        self.rent = rent
    
	def add_smallhouse(self):
		select_newprop = input()
		
	def add_bighotel(self):
		select_property = input("Please type carefully which property you would like to place a red hotel")

class Player:
    def __init__(self):
        self.money = 2500
		self.cards = {}

    def add_prop(self,prop,price):
		self.prop = prop
		self.price = price

