import unittest
from game.cell import Cell
from game.tile import Tile


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
        cell = Cell(multiplier=1, multiplier_type='')
        letter = Tile(letter='p', value=3)

        cell.add_letter(letter=letter)

        self.assertEqual(cell.letter, letter)

    def test_cell_value(self):
        cell = Cell(multiplier=2, multiplier_type='letter')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            6,
        )

    def test_cell_multiplier_word(self):
        cell = Cell(multiplier=2, multiplier_type='word')
        letter = Tile(letter='p', value=3)
        cell.add_letter(letter=letter)

        self.assertEqual(
            cell.calculate_value(),
            3,
        )


    #revisar, Es 16?        
    def test_calculate_word(self):
        cell1 = Cell(multiplier=1, multiplier_type='letter')
        cell2 = Cell(multiplier=2, multiplier_type='word')
        cell3 = Cell(multiplier=1, multiplier_type='letter')
    
        letter1 = Tile(letter='p', value=3)
        letter2 = Tile(letter='y', value=4)
        letter3 = Tile(letter='t', value=1)
        
        cell1.add_letter(letter1)
        cell2.add_letter(letter2)
        cell3.add_letter(letter3)
        
        cell1.word = [cell1, cell2, cell3]
        
        self.assertEqual(
            cell1.calculate_word(),
            16,
        )    

if __name__ == '__main__':
    unittest.main()
