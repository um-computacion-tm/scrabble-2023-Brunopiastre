from game.bagtiles import BagTiles

class Player:
    def __init__(self, id=0):
        self.tiles = []
        self.rack = []
        self.score = 0
        self.id = id    
        

    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))   