class GameObject2:
	def __init__(self,name):
		self.name = name

	def pickUp(self,player):


class Coin(GameObject2):
	def __init__(self,value):
		GameObject2.__init__(self)
		self.value = value

	def spend(self,buyer,seller):
		