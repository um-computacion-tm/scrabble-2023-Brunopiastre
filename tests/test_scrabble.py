import unittest
from unittest.mock import patch
from game.scrabble import ScrabbleGame
from game.tile import Tile
from game.cell import Cell
from game.player import Player
import io
import sys


class TestScrabbleGame(unittest.TestCase):
        
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertIsNotNone(scrabble_game.board)
        self.assertEqual(
            len(scrabble_game.players),
            3,
        )
        self.assertIsNotNone(scrabble_game.bag_tiles)
    
    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)

        scrabble_game.next_turn()

        assert scrabble_game.current_player == 1


    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 0

        scrabble_game.next_turn()

        assert scrabble_game.current_player == 1


   
   
    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = 2

        scrabble_game.next_turn()

        assert scrabble_game.current_player == 0
        

    def test_show_score(self):
        scrabblegame = ScrabbleGame(players_count=3)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabblegame.show_score()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """Su puntaje es : 0
"""
        self.assertEqual(output,expected_output)



    def test_end_game_true(self):
        scrabble_game = ScrabbleGame(players_count=0)
        scrabble_game.bag_tiles.take(100)
        end_game = scrabble_game.end_game()
        self.assertEqual(end_game,True)


    def test_end_game_false(self):
        scrabble_game = ScrabbleGame(players_count=3)
        end_game = scrabble_game.end_game()
        self.assertEqual(end_game,False)


    def test_display_tiles(self):
            player = Player()
            scrabblegame = ScrabbleGame(players_count=3)
            player.tiles = [
                Tile('A', 1),
                Tile('B', 2),
                Tile('C', 3),
                Tile('D', 3),
                Tile('E', 1),
                Tile('F', 4),
                Tile('G', 2),
            ]
            captured_output = io.StringIO()
            sys.stdout = captured_output
            scrabblegame.display_tiles(player)
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            expected_output = """[A,1] [B,2] [C,3] [D,3] [E,1] [F,4] [G,2] """
            self.assertEqual(output,expected_output)




    def test_show_board(self):

        scrabblegame = ScrabbleGame(players_count=3)
        scrabblegame.board.grid = [
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('A', 1)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
            [Cell(letter=Tile('B', 2)) for _ in range(15)],
        ]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabblegame.show_board()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """
  |  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14 
 0| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
 1| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
 2| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
 3| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
 4| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
 5| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
 6| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
 7| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
 8| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
 9| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
10| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
11| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
12| A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1 A:1
13| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
14| B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2 B:2
"""
        self.assertEqual(output,expected_output)





    def test_create_cell_list_horizontal(self):
        scrabbleGame = ScrabbleGame(2)
        word = 'TEST'
        location = (0, 0)
        orientation = 'H'

        cell_list = scrabbleGame.create_cell_list(word, location, orientation)

        expected_cells = [scrabbleGame.board.grid[0][i] for i in range(4)]
        self.assertEqual(len(cell_list), 4)
        self.assertEqual(cell_list, expected_cells)


    def test_create_cell_list_vertical(self):
        scrabbleGame = ScrabbleGame(2)
        word = 'TEST'
        location = (0, 0)
        orientation = 'V'

        cell_list = scrabbleGame.create_cell_list(word, location, orientation)

        expected_cells = [scrabbleGame.board.grid[i][0] for i in range(4)]
        self.assertEqual(len(cell_list), 4)
        self.assertEqual(cell_list, expected_cells)



    @patch('builtins.input', return_value ='A')
    def test_exchange_wildtile(self, mock_input):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.players[scrabbleGame.current_player].tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1),Tile('*', 0)]
        scrabbleGame.exchange_wildtile()
        self.assertEqual(len(scrabbleGame.players[scrabbleGame.current_player].tiles), 6)
        self.assertEqual(scrabbleGame.players[scrabbleGame.current_player].tiles[5].letter, 'A' )
   
    @patch('builtins.input', side_effect =['2', 'A'])
    def test_exchange_wildtile_wrong(self, mock_input):
        scrabbleGame = ScrabbleGame(2)
        scrabbleGame.players[scrabbleGame.current_player].tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1),Tile('*', 0)]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabbleGame.exchange_wildtile()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """
Por favor, ingrese una ficha válida.
"""
        self.assertEqual(output,expected_output)
        


    @patch('builtins.input', return_value='A,B,C')
    def test_ask_tiles_to_change(self, mock_input):
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.players[0].tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1)]
        scrabbleGame.ask_tiles_to_change()
        self.assertEqual(len(scrabbleGame.players[0].tiles), 7)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabbleGame.display_tiles(scrabbleGame.players[0])
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """[A,1] [B,3] [C,3] [D,2] [E,1] """
        self.assertIsNot(output,expected_output)

    @patch('builtins.input', side_effect =['L','A,B,C'])
    def test_ask_tiles_to_change_not_found(self, mock_input):
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.players[0].tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1)]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabbleGame.ask_tiles_to_change()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """Ficha no encontrada: L
"""
        self.assertEqual(output,expected_output)

    @patch('builtins.input', side_effect =['a,%','0'])
    def test_ask_tiles_to_change_not_valid(self, mock_input):
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.players[0].tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1)]
        captured_output = io.StringIO()
        sys.stdout = captured_output
        scrabbleGame.ask_tiles_to_change()
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        expected_output = """
Por favor, ingrese una ficha válida.
"""
        self.assertEqual(output,expected_output)

    @patch('builtins.input', side_effect =['0'])
    def test_ask_tiles_to_change_return(self, mock_input):
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.players[0].tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1)]
        
        self.assertEqual(scrabbleGame.ask_tiles_to_change(), None)




    def test_end(self):
            scrabbleGame = ScrabbleGame(2)
            scrabbleGame.players[0].score = 150
            scrabbleGame.players[1].score = 100
            captured_output = io.StringIO()
            sys.stdout = captured_output
            scrabbleGame.end()
            sys.stdout = sys.__stdout__
            output = captured_output.getvalue()
            expected_output = """Fin del juego\n
Los puntajes finales son:
Jugador      Puntaje
-------      -------
Jugador 0       150
Jugador 1       100
Jugador 0 es el ganador!
"""
            self.assertEqual(output,expected_output)    


if __name__ == '__main__':
    unittest.main()
