import unittest
from game.dictionary import Dictionary
from game.board import Board
from game.cell import Cell
from game.tile import Tile


class TestDictionary(unittest.TestCase):
    
    def test_dictionary_true(self):        
        dictionary = Dictionary()
        file = dictionary.file_path
        board = Board()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('A', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),]
        self.assertEqual(board.check_word(word,file),True)    
    def test_dictionary_false(self):        
        dictionary = Dictionary()
        file = dictionary.file_path
        board = Board()
        word = [
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('C', 1)),
            Cell(letter=Tile('S', 2)),
            Cell(letter=Tile('A', 1)),]
        self.assertEqual(board.check_word(word,file),False)
        
if __name__ == '__main__':
    unittest.main()



