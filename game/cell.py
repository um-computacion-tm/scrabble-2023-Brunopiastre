from game.tile import Tile


class Cell: 
    
    def __init__(self, multiplier=1, multiplier_type='letter', letter=None, active=True):
        self.multiplier = multiplier
        self.multiplier_type = multiplier_type
        self.letter = letter
        self.active = active
    

    def add_letter(self, letter:Tile, board):
        self.letter = letter
        board.is_empty = False

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
    

    def __repr__(self):
            if self.letter:
                return repr(self.letter)
            if self.multiplier > 1:
                return f'{"W" if self.multiplier_type == "word" else "L"}x{self.multiplier}'
            else:
                return '   '



    
        