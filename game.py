from deck import Deck
from player import Player

class Game:

	def __init__(self, numPlayers, numDecks):
		self.team1 = []
		self.team2 = []
		self.deck = Deck(numDecks)
		for i in range(numPlayers):
			if i % 2 == 0:
				self.team1.append(Player(i, input("Player " + str(i) + " name: ")))
			else:
				self.team2.append(Player(i, input("Player " + str(i) + " name: ")))

		# team on defense, 1 or 2, initialized to 0
		self.defense = 0

		self.t1Level = 2
		self.t2Level = 2

		self.points = 0

		self.revealHistory = []

	def __str__(self):
		gameState = ''
		for i in range(len(self.team1)):
			if i == len(self.team1) - 1:
				gameState += self.team1[i].name
			else:
				gameState += self.team1[i].name + ', '
		gameState += ' are on team 1\n'

		for i in range(len(self.team2)):
			if i == len(self.team2) - 1:
				gameState += self.team2[i].name
			else:
				gameState += self.team2[i].name + ', '
		gameState += ' are on team 2\n\n'

		if self.defense == 0:
			gameState += "Game hasn't decided on the defensive team yet\n"
		else:
			gameState += 'Currently on defense is team ' + str(self.defense) + '\n'
			gameState += 'Team ' + str(3 - self.defense) + ' currently has ' + str(self.points) + ' points\n'
			if self.team1[0].hand:
				gameState += "There's " + str(len(self.team1[0].hand)) + ' cards left in the round\n'
			else:
				gameState += 'Currently no one has cards\n'

		return gameState