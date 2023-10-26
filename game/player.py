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


    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)

    