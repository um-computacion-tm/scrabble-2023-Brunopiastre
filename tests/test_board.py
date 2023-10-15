import unittest
from game.board import Board
from game.tile import Tile

class TestBoard(unittest.TestCase):

    def test_init(self):
        board = Board()
        self.assertEqual(
            len(board.grid),
            15,
        )

        self.assertEqual(
            len(board.grid[0]),
            15,
        )
    
    # def test_validate_word_len(self):
    #     position_x = location [0]
    #     position_y = location [1] 





    def test_word_inside_board(self):
            board = Board(is_empty=False)
            word = "Facultad"
            location = (5, 4)
            orientation = "H"
    
            word_is_valid = board.validate_word_inside_board(word, location, orientation)
    
            assert word_is_valid == True


    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "H"

        word_is_valid = board.validate_word_inside_board(word, location, orientation)

        assert word_is_valid == False
    

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1),board)
        assert board.is_empty == False



    def test_place_word_empty_board_horizontal_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_center_board(word, location, orientation)
        assert word_is_valid == True


    
    def test_place_word_empty_board_horizontal_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "H"
        word_is_valid = board.validate_word_center_board(word, location, orientation)
        assert word_is_valid == False



    def test_place_word_empty_board_vertical_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_center_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_empty_board_vertical_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_center_board(word, location, orientation)
        assert word_is_valid == False



    
    

if __name__ == '__main__':

    unittest.main()

