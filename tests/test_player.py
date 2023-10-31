import unittest
from unittest.mock import patch

from game.player import Player
from game.tile import Tile
from game.bagtiles import BagTiles


class TestPlayer(unittest.TestCase):

    def test_init(self):

        player_1 = Player()
        

        self.assertEqual(

            len(player_1.tiles),

            0,

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
        player_1 = Player()
        player_1.tiles = [Tile('C', 1), Tile('A', 1), Tile('S', 1), Tile('A', 1)]
        word = 'CASA'
        result = player_1.validate_tiles(word)
        self.assertEqual(result, True)
        

    def test_validate_tiles_wrong(self):
        player_1 = Player()
        player_1.tiles = []
        word = 'CASA'
        result = player_1.validate_tiles(word)
        self.assertEqual(result, False)


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


if __name__ == '__main__':

    unittest.main()

