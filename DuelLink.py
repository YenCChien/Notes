import random

class Player:
    def __init__(self,cards):
        self.cards = cards
        self.rand()
        self.LP = 4000
        self.deck = self.cards
        self.onhand = []
    def rand(self):
        random.shuffle(self.cards)
    def draw(self,num):
        for c in self.deck[:num]:
            self.onhand.append(c)
            self.deck.remove(c)
    def viewcard(self):
        return self.onhand
    def viewdeck(self):
        return self.deck
    def setLP(self,value):
        self.LP += value
    def __call__(self):
        return self.LP

p1 = Player(['清眼白龍', '力量', '嘎嘎', '真紅眼黑龍', '黑洞'])
p1.viewdeck()
p1.draw(2)
p1.viewdeck()
p1.viewcard()
