import unittest
from game.dictionary import Dictionary
from game.board import Board
from game.cell import Cell
from game.tile import Tile


class TestDictionary(unittest.TestCase):
    pass
    def test_dictionary_true(self):
        board = Board()
        dictionary = Dictionary()
        word = 'CASA'
        file_path = dictionary.file_path
        self.assertEqual(board.check_word(word, file_path), True)

    def test_dictionary_false(self):
        board = Board()
        dictionary = Dictionary()
        word = 'CASSSS'
        file_path = dictionary.file_path
        self.assertEqual(board.check_word(word, file_path), False)
        
if __name__ == '__main__':
    unittest.main()



