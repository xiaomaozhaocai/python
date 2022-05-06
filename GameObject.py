class GameObject:
    def __init__(self,name):
        self.name = name

    def pickUp(self,player):
        pass
        #put code here to add the object
        #to the player's collection


class Coin(GameObject):
    def __init__(self,value):
        GameObject.__init__(self)
        self.value = value

    def spend(self,buyer,seller):
        pass
