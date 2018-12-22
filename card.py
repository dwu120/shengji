class Card:

	FACES = {11: 'J', 12: 'Q', 13: 'K', 14: 'A', 15: 'JO'}
	# 0 spades, 1 hearts, 2 clubs, 3 diamonds, 4 smol joker, 5 big joker
	SUITS = {0: chr(0x2660), 1: chr(0x2661), 2: chr(0x2663), 3: chr(0x2662), 4: chr(0x2726), 5: chr(0x2606)}

	def __init__(self, rank, suit, trump=False):
		self.suit = suit
		self.rank = rank
		self.trump = trump

	def __str__(self):
		if self.rank <= 10:
			return str(self.rank) + self.SUITS[self.suit]
		else:
			return self.FACES[self.rank] + self.SUITS[self.suit]

	def point(self):
		if self.rank == 5:
			return 5
		elif self.rank == 10 or self.rank == 13:
			return 10
		else:
			return 0

	# eariler card played should always go first
	# def __eq__(self, card):
	# 	return self.suit == card.suit and self.rank == card.rank

	# def __ne__(self, card):
	# 	return self.suit != card.suit or self.rank != card.rank

	# def __lt__(self, other):
	# 	if self.trump and other.Trump:
	# 		