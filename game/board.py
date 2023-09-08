from game.cell import Cell
from game.tile import Tile

class Board:
    def __init__(self):
        self.grid = [
            [ Cell(1, '') for _ in range(15) ]
            for _ in range(15)
        ]

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
    

    