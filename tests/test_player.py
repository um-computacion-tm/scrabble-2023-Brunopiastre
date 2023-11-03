import unittest
from unittest.mock import patch

from game.player import Player
from game.tile import Tile
from game.bagtiles import BagTiles
from game.scrabble import ScrabbleGame


class TestPlayer(unittest.TestCase):

    def test_init(self):

        player_1 = Player()
        

        self.assertEqual(

            len(player_1.tiles),

            7,

        )


    def test_player(self):
        player1 = Player()
        self.assertEqual(player1.rack,[])


    def test_player_get_tile(self):
        bag1 = BagTiles()
        player = Player()
        player.get_tiles(3,bag1)
        self.assertEqual(len(player.rack),3)

    
    @patch('builtins.input', return_value='tobias')
    def test_nickname (self, input_patched):
        player = Player()
        player.set_nickname()        
        self.assertEqual(player.nickname, 'tobias')


    def test_increase_score(self):
            player_1=Player()
            player_1.increse_score(2)
            self.assertEqual(player_1.score,2)



    def test_validate_tiles(self):
        location = (7,7)
        orientation = 'H'
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.players[scrabbleGame.current_player].tiles = [Tile('C', 1), Tile('A', 1), Tile('S', 1), Tile('A', 1)]
        word = 'CASA'
        self.assertEqual(scrabbleGame.players[scrabbleGame.current_player].validate_tiles(word, location, orientation, scrabbleGame), True)


    def test_validate_tiles_wrong(self):
        location = (7,7)
        orientation = 'H'
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.players[scrabbleGame.current_player].tiles = []
        word = 'CASA'
        self.assertEqual(scrabbleGame.players[scrabbleGame.current_player].validate_tiles(word, location, orientation, scrabbleGame), False)


    def test_remove_tiles(self):
        player = Player()
        player.tiles = [Tile('A', 1),Tile('B', 3),Tile('C', 3),Tile('D', 2),Tile('E', 1)]
        player.remove_tiles('BAD')
        self.assertEqual(len(player.tiles), 2)
        self.assertEqual(player.tiles[0].letter, 'C')
        self.assertEqual(player.tiles[1].letter, 'E')   


    def test_remove_tiles_not_found(self):
        player = Player()
        player.tiles = [Tile('A', 1), Tile('B', 3), Tile('C', 3), Tile('D', 2), Tile('E', 1)]
        player.remove_tiles('XYZ')
        self.assertEqual(len(player.tiles), 5)



    def test_get_connected_tile(self):
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.board.grid[7][7].add_letter(Tile('C', 1),scrabbleGame.board)
        word = 'CASA'
        location = (7,7)
        orientation = 'H'
        self.assertEqual(scrabbleGame.players[scrabbleGame.current_player].get_connected_tile(word, location, orientation, scrabbleGame), ['C'])



    def test_get_connected_tile2(self):
        scrabbleGame = ScrabbleGame(players_count=3)
        scrabbleGame.board.grid[7][7].add_letter(Tile('C', 1),scrabbleGame.board)
        scrabbleGame.board.grid[7][8].add_letter(Tile('A', 1),scrabbleGame.board)
        scrabbleGame.board.grid[7][9].add_letter(Tile('S', 1),scrabbleGame.board)
        scrabbleGame.board.grid[7][10].add_letter(Tile('A', 1),scrabbleGame.board)
        word = 'CASAS'
        location = (7,7)
        orientation = 'H'
        self.assertEqual(scrabbleGame.players[scrabbleGame.current_player].get_connected_tile(word, location, orientation, scrabbleGame), ['C', 'A', 'S', 'A'])


if __name__ == '__main__':

    unittest.main()

