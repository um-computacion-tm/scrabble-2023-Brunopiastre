from game.tile import Tile


class Cell: 
    
    def __init__(self, letter=None, multiplier=1, multiplier_type='letter', active=True):
        self.letter = letter
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.active= active
        

    def add_letter(self, letter:Tile):
        self.letter = letter

    def calculate_value(self):
        if self.letter is None:
            return 0
        if self.multiplier_type == 'letter':
            return self.letter.value * self.multiplier
        else:
            return self.letter.value


    def calculate_word(self):
        value=0 
        for letras in self.word:
            value_letra = Cell.calculate_value(letras)
            value += value_letra

        for letra in self.word:
            if letra.multiplier_type == "word" and letra.active == True:
                value = value * letra.multiplier
        return value
    



    