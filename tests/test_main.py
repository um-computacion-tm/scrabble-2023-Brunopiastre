import unittest
from unittest.mock import patch, MagicMock
import io
from unittest.mock import patch
from game.main import main
from game.main import put_word
class TestMain(unittest.TestCase):

    @patch('builtins.input', side_effect=['2', '8'])
    def test_main_valid_input(self, mock_input):
        with patch('game.main.ScrabbleGame') as mock_scrabbleGame:
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                main()
                output = fake_stdout.getvalue().strip()
            mock_scrabbleGame.assert_called_once_with(players_count=2)

    @patch('builtins.input', side_effect=['1', '5', '2', 'julian', 'agustin', '8'])
    def test_main_invalid_input(self, mock_input):
        with patch('game.main.ScrabbleGame') as mock_scrabbleGame:
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                main()
                output = fake_stdout.getvalue().strip()
            mock_scrabbleGame.assert_called_once_with(players_count=2)



    @patch('builtins.input', side_effect=['test', '1', '1', 'H'])
    def test_put_word(self, mock_input):
        mock_scrabbleGame = MagicMock()
        mock_scrabbleGame.current_player = 0
        mock_scrabbleGame.players = [MagicMock()]
        mock_scrabbleGame.board.validate_word_placement.return_value = True

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            put_word(mock_scrabbleGame)
            output = fake_stdout.getvalue().strip()

        mock_scrabbleGame.create_tile_list.assert_called_once_with('TEST', mock_scrabbleGame.bag_tiles)
        mock_scrabbleGame.create_cell_list.assert_called_once_with('TEST', ('1', '1'), 'H')
        mock_scrabbleGame.board.validate_word_placement.assert_called_once_with('TEST', ('1', '1'), 'H', mock_scrabbleGame)
        mock_scrabbleGame.board.put_word.assert_called_once()
        mock_scrabbleGame.players[mock_scrabbleGame.current_player].remove_tiles.assert_called_once_with('TEST')
        mock_scrabbleGame.players[mock_scrabbleGame.current_player].increse_score.assert_called_once()

    @patch('builtins.input', side_effect=['test', 'not a number', '1', 'H', 'test', '1', '1', 'H'])
    def test_put_word_with_invalid_input(self, mock_input):
        mock_scrabbleGame = MagicMock()
        mock_scrabbleGame.current_player = 0
        mock_scrabbleGame.players = [MagicMock()]

        try:
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                put_word(mock_scrabbleGame)
                output = fake_stdout.getvalue().strip()
 
        except ValueError:
            print("Se capturó una excepción ValueError")

        mock_scrabbleGame.create_tile_list.assert_called_once_with('TEST', mock_scrabbleGame.bag_tiles)
        mock_scrabbleGame.create_cell_list.assert_called_once_with('TEST', ('1', '1'), 'H')
        mock_scrabbleGame.board.validate_word_placement.assert_called_once_with('TEST', ('1', '1'), 'H', mock_scrabbleGame)
        mock_scrabbleGame.board.put_word.assert_called_once()
        mock_scrabbleGame.players[mock_scrabbleGame.current_player].remove_tiles.assert_called_once_with('TEST')
        mock_scrabbleGame.players[mock_scrabbleGame.current_player].increse_score.assert_called_once()

    @patch('builtins.input', side_effect=['0'])
    def test_put_word_with_zero_input(self, mock_input):
        mock_scrabbleGame = MagicMock()
        mock_scrabbleGame.current_player = 0
        mock_scrabbleGame.players = [MagicMock()]

        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            put_word(mock_scrabbleGame)
            output = fake_stdout.getvalue().strip()

        mock_scrabbleGame.create_tile_list.assert_not_called()
        mock_scrabbleGame.create_cell_list.assert_not_called()
        mock_scrabbleGame.board.validate_word_placement.assert_not_called()
        mock_scrabbleGame.board.put_word.assert_not_called()
        mock_scrabbleGame.players[mock_scrabbleGame.current_player].remove_tiles.assert_not_called()
        mock_scrabbleGame.players[mock_scrabbleGame.current_player].increse_score.assert_not_called()
        
    @patch('game.scrabble.ScrabbleGame', autospec=True)
    def test_put_word_with_invalid_word(self, mock_scrabbleGame):
        mock_board = MagicMock()
        mock_scrabbleGame.return_value.board = mock_board
        mock_board.validate_word_placement.side_effect = [False]
        mock_scrabbleGame.return_value.current_player = 0
        mock_scrabbleGame.return_value.players = [MagicMock()]

        inputs = ['test', '1', '1', 'H', '0']
        input_side_effects = iter(inputs)

        with patch('builtins.input', side_effect=lambda _: next(input_side_effects)) as mock_input:
            with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
                put_word(mock_scrabbleGame.return_value)
                output = fake_stdout.getvalue().strip()

        mock_scrabbleGame.create_cell_list.assert_not_called()
        mock_board.validate_word_placement.assert_called()
        mock_scrabbleGame.return_value.players[mock_scrabbleGame.return_value.current_player].remove_tiles.assert_not_called()
        mock_scrabbleGame.return_value.players[mock_scrabbleGame.return_value.current_player].increse_score.assert_not_called()

if __name__ == '__main__':
    unittest.main()
    