import unittest
from game.tile import  Tile

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_repr(self):
        tile = Tile('A', 1)
        self.assertEqual(repr(tile), 'A:1')

if __name__ == '__main__':

    unittest.main()

