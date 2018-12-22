import random
import time
import os

from deck import Deck
from card import Card
from player import Player 
from game import Game


players = 0
while True:
	try:
		players = int(input("How many players? (Even number, at least 4): "))
		if players % 2 == 0:
			break
		else:
			print("Not a valid input")
	except ValueError:
		print("Not a valid input")

print("Players " + str(list(range(0, players, 2))) + " are team 1")
print("Players " + str(list(range(1, players, 2))) + " are team 2")

decks = 0
while True:
	try:
		decks = int(input("How many decks? (Recommended 1 deck for every 2-4 people): "))
		break
	except ValueError:
		print("Not a valid input")

shengji = Game(players, decks)
print(shengji)

# deck = Deck(decks)

# for card in deck.deck:
# 	print(str(card))

# deck.shuffle()

# for card in deck.deck:
# 	print(str(card))








# def compare_cards(card1, card2, trump = None):
# 	return None

# players = 0
# while True:
# 	try:
# 		players = int(input("How many players? (Even number, at least 4): "))
# 		if players % 2 == 0:
# 			break
# 		else:
# 			print("Not a valid input")
# 	except ValueError:
# 		print("Not a valid input")

# print("Players " + str(list(range(0, players, 2))) + " are team 1")
# print("Players " + str(list(range(1, players, 2))) + " are team 2")

# decks = 0
# while True:
# 	try:
# 		decks = int(input("How many decks? (Recommended 1 deck for every 2-4 people): "))
# 		break
# 	except ValueError:
# 		print("Not a valid input")

# # print(players, decks)

# deck = []

# deck.append(('A', chr(0x2660)))
# deck.append(('K', chr(0x2660)))
# deck.append(('Q', chr(0x2660)))
# deck.append(('J', chr(0x2660)))
# for i in range(10, 1, -1):
# 	deck.append((str(i), chr(0x2660)))

# deck.append(('A', chr(0x2661)))
# deck.append(('K', chr(0x2661)))
# deck.append(('Q', chr(0x2661)))
# deck.append(('J', chr(0x2661)))
# for i in range(10, 1, -1):
# 	deck.append((str(i), chr(0x2661)))

# deck.append(('A', chr(0x2662)))
# deck.append(('K', chr(0x2662)))
# deck.append(('Q', chr(0x2662)))
# deck.append(('J', chr(0x2662)))
# for i in range(10, 1, -1):
# 	deck.append((str(i), chr(0x2662)))

# deck.append(('A', chr(0x2663)))
# deck.append(('K', chr(0x2663)))
# deck.append(('Q', chr(0x2663)))
# deck.append(('J', chr(0x2663)))
# for i in range(10, 1, -1):
# 	deck.append((str(i), chr(0x2663)))

# deck.append(('JO', chr(0x2726)))
# deck.append(('JO', chr(0x2606)))

# deck = deck * decks

# random.shuffle(deck)

# highest = 0
# starter = 0
# counter = 0
# while counter < players:
# 	card = random.randrange(len(deck))
# 	input("Player " + str(counter) + " hit enter to draw a card: ")
# 	print("Player " + str(counter) + " drew a", deck[card])
# 	if deck[card][0] not in ['A', 'K', 'Q', 'J', 'JO']:
# 		if highest < int(deck[card][0]):
# 			highest = int(deck[card][0])
# 			starter = counter
# 			if highest == 10:
# 				counter = players
# 	if counter == players - 1 and highest == 0:
# 		counter = -1
# 	counter += 1

# time.sleep(5)
# os.system('clear')
# print("Player " + str(starter) + " starts", flush=True)
# input("Player " +str((starter - 1) % players) + " hit enter to cut the deck: ")

# rand = random.randrange(len(deck))
# deck = deck[rand:] + deck[:rand]

# hands = []
# canShow = []
# team1 = 2
# team2 = 2
# defense = 0
# trumpSuit = None
# trumpCount = 0 

# for i in range(players):
# 	hands.append([])
# 	canShow.append([])

# while len(deck) - players >= 6:
# 	for i in range(starter, starter + players, 1):
# 		card = deck.pop()
# 		hands[i % players].append(card)
# 		if card[0] == str(team1) or card[0] == str(team2):
# 			canShow[i % players].append(card[1])
# 		print("Player " + str(i % players) + " drew a " + card[0] + card[1])
# 		if canShow[i % players]:
# 			print("Player " + str(i % players) + " can reveal " + str(canShow[i % players]) + " as trump")
# 			show = input("Reveal? (index of list, or n): ")
# 			try:
# 				trump = canShow[i % players][int(show)]
# 			except:
# 				print("Nothing was revealed")
# 			# print(trump)

# 		time.sleep(1)

# for i in range(players):
# 	print(len(hands[i]))
# 	print(hands[i])
# print(len(deck))
# print(deck)












# if __name__ == "__main__":
# 	gamesetup()
# 	rungame()


# for card in deck:
# 	if card[0] == '10' or card[0] == 'JO':
# 		print(card[0] + card[1])
# 	else:
# 		print(card[0], card[1])


# print(chr(0x2660))
# print(chr(0x2661))
# print(chr(0x2662))
# print(chr(0x2663))
# print(chr(0x2664))
# print(chr(0x2665))
# print(chr(0x2666))
# print(chr(0x2667))