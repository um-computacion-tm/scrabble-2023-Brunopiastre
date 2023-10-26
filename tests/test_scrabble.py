import unittest
from game.scrabble import ScrabbleGame
# from game.board import Board
from game.tile import Tile
# from game.cell import Cell
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



    def test_game_over(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.bag_tiles = []  
        self.assertTrue(scrabble_game.game_over())



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

if __name__ == '__main__':
    unittest.main()
