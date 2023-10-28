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


if __name__ == '__main__':

    unittest.main()

