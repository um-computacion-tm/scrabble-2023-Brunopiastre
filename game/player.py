from game.bagtiles import BagTiles

class Player:
    def __init__(self, id=0, nickname = 'apodo'):
        self.tiles = []
        self.rack = []
        self.score = 0
        self.id = id    
        self.nickname = nickname

    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))  

    def set_nickname(self):
        self.nickname = str(input('Ingrese su apodo: '))
 

    def increse_score(self,amount):
        self.amount=amount
        self.score+=amount



    def validate_tiles(self, word):
        return set(word).issubset(tile.letter for tile in self.tiles)

    
    def remove_tiles(self, word):
        self.tiles = [tile for tile in self.tiles if tile.letter not in word]
