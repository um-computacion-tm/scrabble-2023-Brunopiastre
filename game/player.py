from game.bagtiles import BagTiles

class Player:
    def __init__(self, id=0, nickname = 'apodo'):
        bagTiles= BagTiles()
        self.tiles = []
        self.rack = []
        self.score = 0
        self.id = id    
        self.nickname = nickname
        self.tiles = bagTiles.take(7)

    def get_tiles(self,amount,bag=BagTiles):
        for _ in range(amount):
            self.rack.append(bag.take(1))  

    def set_nickname(self):
        self.nickname = str(input('Ingrese su apodo: '))
 

    def increse_score(self,amount):
        self.amount=amount
        self.score+=amount



    
    def validate_tiles(self, word, location, orientation, scrabbleGame):
        tiles = [tile.letter for tile in self.tiles]
        tiles.extend(self.get_connected_tile(word, location, orientation, scrabbleGame))
        for letter in word:
            if letter not in tiles:
                return False
            tiles.remove(letter)
        return True

    
    def remove_tiles(self, word):
        self.tiles = [tile for tile in self.tiles if tile.letter not in word] #


    def get_connected_tile(self, word, location, orientation, scrabbleGame):
        word = word.upper()
        x, y = location
        x, y= int(x), int(y)
        lista = []
        for letter in word:
            if scrabbleGame.board.grid[x][y].letter and scrabbleGame.board.grid[x][y].letter.letter == letter:
                lista.append(letter)
            if orientation == 'H':
                y += 1
            elif orientation == 'V':
                x += 1

        return lista
    


    