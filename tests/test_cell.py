import unittest
from game.cell import Cell
from game.tile import Tile
from game.board import Board


class TestCell(unittest.TestCase):
    def test_init(self):
        cell = Cell(multiplier=2, multiplier_type='letter')

        self.assertEqual(
            cell.multiplier,
            2,
        )
        self.assertEqual(
            cell.multiplier_type,
            'letter',
        )
        self.assertIsNone(cell.letter)
        self.assertEqual(
            cell.calculate_value(),
            0,
        )

    def test_add_letter(self):
        board = Board()
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter,board)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        board = Board() 
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter, board)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        board = Board ()
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter, board)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )

    def test_repr(self):
        cell = Cell(2, "word")
        self.assertEqual(repr(cell), 'Wx2')
    
    def test_repr2(self):
        cell = Cell(1, "word")
        self.assertEqual(repr(cell), '   ')

    def test_repr3(self):
        cell = Cell(1, "word", letter=("A", 1))
        self.assertEqual(repr(cell), "('A', 1)")

    def test_repr4(self):
        cell = Cell(2, "letter")
        self.assertEqual(repr(cell), 'Lx2')

if __name__ == '__main__':
    unittest.main()
