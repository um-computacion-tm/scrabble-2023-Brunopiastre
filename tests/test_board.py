import unittest
from game.board import Board
from game.tile import Tile
from game.scrabble import ScrabbleGame


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
   

    def test_word_inside_board(self):
            board = Board(is_empty=False)
            word = "Facultad"
            location = (5, 4)
            orientation = "H"
    
            word_is_valid = board.validate_word_len(word, location, orientation)
    
            assert word_is_valid == True


    def test_word_out_of_board(self):
        board = Board()
        word = "Facultad"
        location = (14, 4)
        orientation = "V"

        word_is_valid = board.validate_word_len(word, location, orientation)

        assert word_is_valid == False
    

    def test_board_is_empty(self):
        board = Board()
        assert board.is_empty == True

    def test_board_is_not_empty(self):
        board = Board()
        board.grid[7][7].add_letter(Tile('C', 1),board)
        assert board.is_empty == False





    def test_place_word_empty_board_horizontal_center_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    
    
    def test_place_word_empty_board_horizontal_inside_fine(self):
        board = Board()
        word = "Facultad"
        location = (7, 4)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True


    
    def test_place_word_board_horizontal_center_wrong(self):
        board = Board()
        word = "australopitecus"
        location = (7, 7)
        orientation = "H"
        word_is_valid = board.validate_word_len(word, location, orientation)
        assert word_is_valid == False





    def test_place_word_empty_board_horizontal_inside_wrong(self):
        board = Board()
        word = "gato"
        location = (7,13)
        orientation = "H"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False
        


    def test_place_word_empty_board_vertical_center_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_empty_board_vertical_center_inside_fine(self):
        board = Board()
        word = "Facultad"
        location = (4, 7)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == True
    
    def test_place_word_empty_board_vertical_center_wrong(self):
        board = Board()
        word = "Facultad"
        location = (2, 4)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False



    def test_place_word_empty_board_vertical_inside_fine(self):
        board = Board()
        word = "hipoacustico"
        location = (3,3)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False

    def test_place_word_board_vertical_inside_fine(self):
        board = Board()
        word = "hipoacustico"
        location = (3,3)
        orientation = "V"
        word_is_valid = board.validate_word_len(word, location, orientation)
        assert word_is_valid == True

    def test_place_word_empty_board_vertical_inside_wrong(self):
        board = Board()
        word = "hipoacustico"
        location = (3, 9)
        orientation = "V"
        word_is_valid = board.validate_word_inside_board(word, location, orientation)
        assert word_is_valid == False



    
    def test_place_word_not_empty_board_horizontal_fine(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.board.grid[7][7].add_letter(Tile('C', 1), scrabbleGame.board)
        scrabbleGame.board.grid[8][7].add_letter(Tile('A', 1), scrabbleGame.board) 
        scrabbleGame.board.grid[9][7].add_letter(Tile('S', 1), scrabbleGame.board) 
        scrabbleGame.board.grid[10][7].add_letter(Tile('A', 1), scrabbleGame.board) 
        word = "Facultad"
        location = (8, 6)
        orientation = "H"
        word_is_valid = scrabbleGame.board.validate_word_is_connected(word, location, orientation, scrabbleGame) 
        self.assertEqual(word_is_valid, True)

    def test_place_word_not_empty_board_horizontal_wrong(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.board.grid[7][7].add_letter(Tile('C', 1), scrabbleGame.board)
        scrabbleGame.board.grid[8][7].add_letter(Tile('A', 1), scrabbleGame.board) 
        scrabbleGame.board.grid[9][7].add_letter(Tile('S', 1), scrabbleGame.board) 
        scrabbleGame.board.grid[10][7].add_letter(Tile('A', 1), scrabbleGame.board) 
        word = "oraculo"
        location = (8, 6)
        orientation = "H"
        word_is_valid = scrabbleGame.board.validate_word_is_connected(word, location, orientation, scrabbleGame)
        self.assertEqual(word_is_valid, False)

        
    def test_place_word_not_empty_conected_board_vertical_fine(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.board.grid[7][7].add_letter(Tile('C', 1),scrabbleGame.board)
        scrabbleGame.board.grid[7][8].add_letter(Tile('A', 1),scrabbleGame.board)
        scrabbleGame.board.grid[7][9].add_letter(Tile('S', 1),scrabbleGame.board)
        scrabbleGame.board.grid[7][10].add_letter(Tile('A', 1),scrabbleGame.board)
        word = "Facultad"
        location = (6, 8)
        orientation = "V"
        word_is_valid = scrabbleGame.board.validate_word_is_connected(word, location, orientation, scrabbleGame)
        assert word_is_valid == True

    def test_place_word_not_empty_not_conected_board_vertical_wrong(self):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.board.grid[7][7].add_letter(Tile('C', 1), scrabbleGame.board)
        scrabbleGame.board.grid[7][8].add_letter(Tile('A', 1), scrabbleGame.board) 
        scrabbleGame.board.grid[7][9].add_letter(Tile('S', 1), scrabbleGame.board) 
        scrabbleGame.board.grid[7][10].add_letter(Tile('A', 1), scrabbleGame.board) 
        word = "oraculo"
        location = (6, 8)
        orientation = "V"  
        word_is_valid = scrabbleGame.board.validate_word_is_connected(word, location, orientation, scrabbleGame)
        self.assertEqual(word_is_valid, False)

    def test_put_word_horizontal(self):
        game = ScrabbleGame(2)
        game.board.put_word(game.create_tile_list('HELLO', game.bag_tiles), (7, 7), 'H')
        self.assertEqual(game.board.grid[7][7].letter.letter, 'H')
        self.assertEqual(game.board.grid[7][8].letter.letter, 'E')
        self.assertEqual(game.board.grid[7][9].letter.letter, 'L')
        self.assertEqual(game.board.grid[7][10].letter.letter, 'L')
        self.assertEqual(game.board.grid[7][11].letter.letter, 'O')

            
    def test_put_word_vertical(self):
        game = ScrabbleGame(2)
        game.board.put_word(game.create_tile_list('HELLO', game.bag_tiles), (7, 7), 'V')
        self.assertEqual(game.board.grid[7][7].letter.letter, 'H')
        self.assertEqual(game.board.grid[8][7].letter.letter, 'E')
        self.assertEqual(game.board.grid[9][7].letter.letter, 'L')
        self.assertEqual(game.board.grid[10][7].letter.letter, 'L')
        self.assertEqual(game.board.grid[11][7].letter.letter, 'O')

    



    def test_validate_word_placement(self):
        game = ScrabbleGame(2)
        player = game.players[0]
        player.tiles = [Tile('H', 1), Tile('E', 1), Tile('L', 1), Tile('O', 1)]

        tests = [
            ('HELLO', (7, 7), 'H', True),

            ('HELLO', (7, 12), 'H', False),

            ('SCRABBLE', (8, 6), 'H', False),

            ('GAME', (7, 7), 'H', False),


        ]

    def test_validate_word_placement_not_empty(self):
        game = ScrabbleGame(2)
        game.board.is_empty = False
        game.board.grid[7][7].add_letter(Tile('C', 1), game.board)
        game.board.grid[7][8].add_letter(Tile('A', 1), game.board) 
        game.board.grid[7][9].add_letter(Tile('S', 1), game.board) 
        game.board.grid[7][10].add_letter(Tile('A', 1), game.board) 
        game.players[0].tiles = [ Tile('A', 1), Tile('S', 1), Tile('A', 1)]

        assert game.board.validate_word_placement('CASA', (7, 7), 'V', game) == True

    

 

if __name__ == '__main__':

    unittest.main()



