from game.cell import Cell  


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
        position_x = location[0]
        position_y = location[1]
        self.word = word

        len_word = len(word)

        if orientation == "H":

            if position_y + len_word > 15:

                return False

            else:

                return True

        else:   
            if position_x + len_word > 15:
                return False
            else:
                return True
            
    # def empty(self):
    #     if self.grid[7][7].letter == None:
    #         self.is_empty = True
    #     else:
    #         self.is_empty = False



    def check_word(self, word, file_path):
        string_word = ''
        for aux in word:
            string_word += aux.letter.letter
        string_word = string_word.lower()
        with open(file_path, "r") as file:
            words = file.read().splitlines()
            if string_word in words:
                return True
            else:
                return False


    def validate_word_inside_board(self, word, location, orientation):

            position_x = location[0]
            position_y = location[1]
            len_word = len(word)
            x = position_x
            y = position_y
            if (self.is_empty == True) & (orientation == 'H'):
                for i in range(len_word):
                    y += 1
                    if (x==7) & (y==7):
                        return True
                return False 
            if (self.is_empty == True) & (orientation == 'V'):
                for i in range(len_word):
                    x += 1
                    if (x==7) & (y==7):
                        return True
                return False
                



    def validate_word_is_connected(self, word, location, orientation):
        word = word.upper()
        x, y = location

        for letter in word:
            if self.grid[x][y].letter and self.grid[x][y].letter.letter == letter:
                return True

            if orientation == 'H':
                y += 1
            elif orientation == 'V':
                x += 1

        return False




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
