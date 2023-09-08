import unittest
from game.bagtiles import BagTiles
from unittest.mock import patch
from game.tile import Tile


class TestBagTiles(unittest.TestCase):

    @patch('random.shuffle')

    def test_bag_tiles(self, patch_shuffle):

        bag = BagTiles()

        self.assertEqual(

            len(bag.tiles),

            100,

        )

        self.assertEqual(

            patch_shuffle.call_count,

            1,

        )

        self.assertEqual(

            patch_shuffle.call_args[0][0],

            bag.tiles,

        )


    def test_take(self):

        bag = BagTiles()

        tiles = bag.take(7)

        self.assertEqual(

            len(bag.tiles),

            93,

        )

        self.assertEqual(

            len(tiles),

            7,

        )



    def test_put(self):

        bag = BagTiles()

        put_tiles = [Tile('Z',10), Tile('Y',4)]

        bag.put(put_tiles)

        self.assertEqual(

            len(bag.tiles),

            102,

        )





if __name__ == '__main__':

    unittest.main()

