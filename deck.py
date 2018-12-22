import random
import itertools
from card import Card

class Deck:

	def __init__(self, numDecks):
		self.deck = []
		for i in range(numDecks):
			for card in itertools.product(range(2, 15), range(4)):
				self.deck.append(Card(card[0], card[1]))
			self.deck.append(Card(15, 4, trump=True))
			self.deck.append(Card(15, 5, trump=True))
		self.trump = None
		self.level = 0

	def __str__(self):
		return str(self.deck)

	def shuffle(self):
		random.shuffle(self.deck)

	def cut(self):
		rand = random.randrange(len(deck))
		self.deck = self.deck[rand:] + self.deck[:rand]

	def update_trump(trump, level):
		self.trump = trump
		self.level = level
		for card in self.deck:
			if card.suit == self.trump or card.rank == self.level or card.rank == 15:
				card.trump = True
			else:
				card.trump = False

	#returns a new sorted version of the deck: 0 list jokers and trumps
	#1-4 lists suits
	# def organize(self):
	# 	pass