from game.cell import Cell  

class Board:
    
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]


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
    








    def validate_word (self, word, file):
        wordletter = ""
        for i in word:
            wordletter += i.letter.letter
        wordletter = wordletter.lower()
        with open(file, 'r') as archivo:
            palabras = archivo.read().splitlines()
            if wordletter == palabras:
                return True
            else:
                return False
    



    def validate_word_inside_board(self, word, location, orientation):

        position_x = location[0]

        position_y = location[1]

        len_word = len(word)

        if orientation == "H":

            if position_x + len_word > 15:

                return False

            else:

                return True

        else:
            if position_y + len_word > 15:
                return False
            else:
                return True

            pass


    #   ARREGLAR este o el test
    def empty(self):
        if self.grid[7][7].letter == None:
            self.is_empty = True
        else:
            self.is_empty = False
    