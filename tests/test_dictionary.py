import unittest
from game.dictionary import Dictionary
from game.board import Board
from game.cell import Cell
from game.tile import Tile


class TestDictionary(unittest.TestCase):

    def test_validate_word_true(self):
      # file = dictionary_file_path #que hace? 
       diccionario = Dictionary()
       board = Board()
       word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
    
       file = diccionario.dictionary 
       result = board.validate_word(word, file)
       self.assertEqual(result, True)


    def test_validate_word_false(self):
        #file = dictionary_file_path #que hace? 
       diccionario = Dictionary()
       board = Board()
       word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),
        ]
    
       file = diccionario.dictionary 
       result = board.validate_word(word, file)
       self.assertEqual(result, False)




        
if __name__ == '__main__':
    unittest.main()



