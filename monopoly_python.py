# simple text based monopoly

import math
import time 
import cmath
from random import *

# Variables and Booleans
global player_one_pos
player_one_pos = 0
game_run = True
global active
active = 0
global inactive
inactive = 1
player_one = False
player_two = False
ai = False
#

# Dictionarys and Stored Game Data 

properties = dict = {1: "Vine Street", 3: "Coventry Street", 6: "Cester Square", 8: "Bow Street" , 9: "Chapel Road", 
11: "Angel Island", 13: "Trafalgar Square", 14: "North Avenue", 16: "Rough Street", 18: "Fleet Street", 
19: "Old Kent Road", 21: "Whitehall", 23: "Penton Road", 24: "Pall Mall", 26: "Bond Street", 27: "Strand", 29: "Regent Street",
31: "East Road", 32: "Piccadilly", 34: "Oxford Street", 37: "Park Lane", 39: "Mayfair", "Rent_Brown": 5, "Rent_LBlue": 15,
"Rent_Pink": 25, "Rent_Orange": 50, "Rent_Red": 75, "Rent_Yellow": 90, "Rent_Green": 105, "Rent_Blue": 125, "Buy_Brown": 50, "Buy_LBlue": 90, "Buy_Pink": 125,
"Buy_Orange": 150, "Buy_Red": 175, "Buy_Yellow": 200, "Buy_Green": 225, "Buy_Blue": 250}

players = dict = {0: "Player One", 1: "Player Two"}

postions = dict = {0: 0, 1: 0, 2: 0}

money = dict = {0: 2500, 1: 2500}

player_prop = {0:{}, 1:{}}
#

# Functions

def GameOptions(): # prints the game options easier and is established as a function 
	print("1: Roll Dice")
	print("2: Edit Owned Properties")
	print("3: Make Trade")
	print("4: Help")
	print("5: End Move")
()

def EndMove(): # acts as the ending move selection
	print("2: Edit Owned Properties")
	print("3: Make Trade")
	print("4: Help")
	print("5: End Move")
()
#

print("Welcome to Monopoly (TM) text edition.") # introduction 
start = input("Press Enter to Play")
print("Each player will start with $1000 Monopoly Dollars, the goal is to bankrupt the other players") # simple instructions XD
input("Press Enter") 
print("If at anytime you need help feel free to select the help option.")
input("Press Enter")
print("The game will now begin. It is player one's turn.")
while game_run == True: # loops the process over and over again so the game can run out (timer features coming soon)
	GameOptions()
	game_running = True
	choice = int(input("Select a option ")) # gets user imput
	if choice == 1:
		dice_roll = randint(1,12) # random number / dice roll
		if game_running == True:
			for p in postions: # gets the user that is currently active and sets a variable that is then used later
				if p == active:
					number = postions.get(p)
			for t in players:
				if active == t: # checks which plater is active by scrolling through the dcitionary searching for the equal player
					words = players[active]
					print(words)
					print (dice_roll)
					for n in properties:
						if n == number:
							final = properties.get(n)
							print(final)
			number += dice_roll # takes the dice roll and sets it equal the number
			postions.update({active: number}) # overwrites the current values within the dictionary (Postions) with the playter total move postion (line 73 and 80)
			x = postions.get(active)
			for b in properties:
				if b == number:
					prop_create = properties.get(b)
			for r in properties:
				for y in (player_prop[active]):
					if r == x and r == y:
						print("You owe" + words)
					for t in money:
						amount_money = money.get(active)
					if r == 1 or 3:
						new_total = amount_money - 5
						money.update({active: new_total})
					elif r == 6 or 8 or 9:
						new_total = amount_money - 15
						money.update({active: new_total})
					elif r == 11 or 13 or 14:
						new_total = amount_money - 25
						money.update({active: new_total})
					elif r == 16 or 18 or 19:
						new_total = amount_money - 50
						money.update({active: new_total})
					elif r == 21 or 23 or 24:
						new_total = amount_money - 75
						money.update({active: new_total})
					elif r == 26 or 27 or 29:
						new_total = amount_money - 90
						money.update({active: new_total})
					elif r == 31 or 32 or 34:
						new_total = amount_money - 105
						money.update({active: new_total})
					elif r == 37 or 39:
						new_total = amount_money - 125
						money.update({active: new_total})
				else:
					if r == number:
						confirm = input("Would you like to purchase " + "Please enter Yes or No")
						if confirm == "Yes":
							for n in properties:
								if n == number:
									final = properties.get(n)
								player_prop[active][r] = final
								print(player_prop[active])
					if x >= 40: # ensures that the player remains on board spaces and not just random places
						overage = number - 40 #
						pass_go = amount_money + 200
						money.update({active: pass_go})
						number = overage 
						postions.update({active: number})
					print(postions)
			EndMove()
			choice = int(input("Select a option")) # gets user input
			if choice == 5: # transfers turn over to the next player
				active += 1
			if inactive == 1:
				inactive = 0
			elif inactive == 0:
				inactive = 1
			if active == 2:
				active = 0

	()
			
	if choice == 2:
		print("Edit Owned Properties")
	()

	if choice == 3:
		print("Make Trade")
	()

	if choice == 4:
		print("Help")
	()



