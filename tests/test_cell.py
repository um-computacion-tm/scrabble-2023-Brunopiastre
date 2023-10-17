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


    def test_calculate_word():
    # Test case 1: Single-letter word
    cell = Cell('A', 1, None)
    word = Word([cell])
    assert word.calculate_word() == 1

    # Test case 2: Word with different letter values
    cell1 = Cell('H', 1, None)
    cell2 = Cell('E', 1, None)
    cell3 = Cell('L', 1, None)
    cell4 = Cell('L', 1, None)
    cell5 = Cell('O', 1, None)
    word = Word([cell1, cell2, cell3, cell4, cell5])
    assert word.calculate_word() == 31

    # Test case 3: Word with letter and word multipliers
    cell1 = Cell('D', 2, 'word')
    cell2 = Cell('O', 1, None)
    cell3 = Cell('G', 3, 'word')
    word = Word([cell1, cell2, cell3])
    assert word.calculate_word() == 18

    # Test case 4: Word with inactive letter
    cell1 = Cell('A', 1, None)
    cell2 = Cell('B', 2, 'word', False)
    cell3 = Cell('C', 1, None)
    word = Word([cell1, cell2, cell3])
    assert word.calculate_word() == 2

    print("All test cases passed")


        
if __name__ == '__main__':
    unittest.main()
