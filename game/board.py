from game.cell import Cell 
from game.dictionary import Dictionary


triple_word_multiplier = ((0, 0), (7, 0), (14, 0), (0, 7), (14, 7), (0, 14), (7, 14), (14, 14))
double_word_multiplier = ((1, 1), (2, 2), (3, 3), (4, 4), (1, 13), (2, 12), (3, 11), (4, 10), (13, 1), (12, 2), (11, 3),
                     (10, 4), (13, 13), (12, 12), (11, 11), (10, 10))
triple_letter_multiplier = ((1, 5), (1, 9), (5, 1), (5, 5), (5, 9), (5, 13), (9, 1), (9, 5), (9, 9), (9, 13), (13, 5),
                       (13, 9))
double_letter_multiplier = ((0, 3), (0, 11), (2, 6), (2, 8), (3, 0), (3, 7), (3, 14), (6, 2), (6, 6), (6, 8), (6, 12),
                       (7, 3), (7, 11), (8, 2), (8, 6), (8, 8), (8, 12), (11, 0), (11, 7), (11, 14), (12, 6), (12, 8),
                       (14, 3), (14, 11))


class Board:
    
    def __init__(self, is_empty=True):
        self.is_empty = is_empty  
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]
        self.add_multiplier()


    def calculate_word_value(self,word):
        aux = 0
        suma = 0
        list = []
    
        
        for aux in range(len(word)):          
            
            if word[aux].active == False:
                    word[aux].multiplier = 1        
            
            if word[aux].multiplier_type == 'letter':
                    suma += (word[aux].letter.value * word[aux].multiplier)
            
            else:
                suma += word[aux].letter.value
                list.append(aux)
        for _ in list:
            suma = suma * word[_].multiplier
        return suma
    



    def validate_word_len(self, word, location, orientation):
        position_x, position_y = location
        position_x, position_y = int(position_x), int(position_y)
        len_word = len(word)

        if orientation == "H" and position_y + len_word <= 15:
            return True
        elif orientation == 'V' and position_x + len_word <= 15:
            return True

        return False


    def check_word(self,word, file_path):
        wordletter = word
        wordletter = wordletter.lower()
        with open(file_path, "r") as file:
            words = file.read().splitlines()
            if wordletter in words:
                return True
            else:
                return False

    def validate_word_inside_board(self, word, location, orientation):
            x, y= location
            x, y= int(x), int(y)
            len_word = len(word)
            if (self.is_empty == True):
                for i in range(len_word):
                    if ((x==7) & (y==7)) & (self.validate_word_len(word, location, orientation)== True):
                           return True
                    if (orientation == 'H'):
                        y += 1
                    else:
                        x += 1
                return False
            return True


    def validate_word_is_connected(self, word, location, orientation, scrabble_game):
            if not self.is_empty:
                current_player = scrabble_game.players[scrabble_game.current_player]
                connected_tile = current_player.get_connected_tile(word, location, orientation, scrabble_game)
                if connected_tile == []:
                    return False
                return True
            return True 




    def add_multiplier(self):
        multipliers = {
            triple_word_multiplier: 3,
            double_word_multiplier: 2,
            triple_letter_multiplier: 3,
            double_letter_multiplier: 2
        }

        for coordinates, multiplier in multipliers.items():
            for coordinate in coordinates:
                self.set_Cell_multiplier(coordinate, "word" if "word" in coordinates else "letter", multiplier)




    def set_Cell_multiplier(self, coordinate, multiplier_type, multiplier_value):
        self.grid[coordinate[0]][coordinate[1]].multiplier_type = multiplier_type
        self.grid[coordinate[0]][coordinate[1]].multiplier = multiplier_value



    def put_word(self, word, location, orientation):
        self.is_empty = False
        x, y = location
        x, y = int(x), int(y)
        for tile in word:
            self.grid[x][y].letter = tile
            if orientation == 'H':
                y += 1
            else:
                x += 1


    def validate_word_placement(self, word, location, orientation, scrabbleGame):
        if not self.validate_word_is_connected(word, location, orientation, scrabbleGame) or \
        not self.validate_word_len(word, location, orientation) or \
        not self.validate_word_inside_board(word, location, orientation) or \
        not self.check_word(word, Dictionary().file_path) or \
        not scrabbleGame.players[scrabbleGame.current_player].validate_tiles(word, location, orientation, scrabbleGame): #PROBAR CON TODOS LOS AMARILLOS Y VALIDATE TILES
            return False
        return True