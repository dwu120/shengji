import card

class Player:

	def __init__(self, pid, name):
		self.id = pid
		self.name = name
		self.hand = []

	def deal_card(card):
		self.hand.append(card)

	def play_cards(cards):
		toPlay = []
		for card in cards:
			try:
				self.hand.remove(card)
				toPlay.append(card)
			except:
				print("There was a problem with your cards. Try playing other cards.")
				self.hand.extend(toPlay)
				return None
		return toPlay