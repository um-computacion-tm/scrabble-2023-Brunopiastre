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
    
    def test_validate_word_len(self):
        board = Board()
        wordletter = "gato"





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


    def test_place_word_not_empty_conected_board_horizontal_fine(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1),board)
        board.grid[8][7].add_letter(Tile('A', 1),board)
        board.grid[9][7].add_letter(Tile('S', 1),board)
        board.grid[10][7].add_letter(Tile('A', 1),board)
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = board.validate_word_is_connected(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_not_empty_not_conected_board_horizontal_wrong(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('T', 1),board)
        board.grid[8][7].add_letter(Tile('R', 1),board)
        board.grid[9][7].add_letter(Tile('E', 1),board)
        board.grid[10][7].add_letter(Tile('S', 1),board)
        word = "Facultad"
        location = (9, 6)
        orientation = "H"
        word_is_valid = board.validate_word_is_connected(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_not_empty_conected_board_vertical_fine(self):
        board = Board() 
        board.grid[7][7].add_letter(Tile('C', 1),board)
        board.grid[7][8].add_letter(Tile('A', 1),board)
        board.grid[7][9].add_letter(Tile('S', 1),board)
        board.grid[7][10].add_letter(Tile('A', 1),board)
        word = "Facultad"
        location = (6, 8)
        orientation = "V"
        word_is_valid = board.validate_word_is_connected(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_not_empty_not_conected_board_vertical_wrong(self):
        board = Board() 
        board.grid[7][7].add_letter(Tile('C', 1),board)
        board.grid[7][8].add_letter(Tile('A', 1),board)
        board.grid[7][9].add_letter(Tile('S', 1),board)
        board.grid[7][10].add_letter(Tile('A', 1),board)
        word = "Facultad"
        location = (6,9)
        orientation = "V"
        word_is_valid = board.validate_word_is_connected(word, location, orientation)
        assert word_is_valid == False

    # def test_place_tile(self):
    #     board = Board()
    #     tile = Tile('A', 1)
    #     self.assertTrue(board.place_tile(7, 7, tile))
    #     self.assertFalse(board.place_tile(7, 7, tile))

    # def test_clear_cell_valid(self):
    #     board = Board()
    #     tile = Tile('A', 1)

    #     # Colocamos una ficha en una celda
    #     board.place_tile(7, 7, tile)
    #     # Luego la limpiamos
    #     board.clear_cell(7, 7)
    #     # Comprobamos que la celda esté vacía     
    #     self.assertIsNone(board.grid[7][7].letter)

    # def test_clear_cell_invalid(self):
    #     board = Board()
    #     result = board.clear_cell(16, 16)
    #     self.assertFalse(result)


if __name__ == '__main__':

    unittest.main()

