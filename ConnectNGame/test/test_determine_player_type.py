import unittest
from unittest.mock import patch
from determine_player_type import determine_player_type
from .print_capturer import PrintCapturer


class TestPlayerType(unittest.TestCase):

    def test_determine_player_type(self):
        player_type = 's'
        with patch('determine_player_type.input', side_effect = player_type):
            ans = determine_player_type(1)
        self.assertEqual(3, ans)

    def test_determine_bad_player_type(self):
        capture = PrintCapturer()
        player_type = ['bugs', 'random']
        with patch('determine_player_type.input', side_effect=player_type):
            with patch('determine_player_type.print', side_effect=capture):
                determine_player_type(1)
                outputs = ['bugs is not one of Human or Random or Simple. Please try again.\n']
                self.assertEqual(outputs, capture.output)

    def test_multiple_player_types(self):
        capture = PrintCapturer()
        player_type = ['human random', 'h']
        with patch('determine_player_type.input', side_effect=player_type):
            with patch('determine_player_type.print', side_effect=capture):
                determine_player_type(1)
                outputs = ['human random is not one of Human or Random or Simple. Please try again.\n']
                self.assertEqual(outputs, capture.output)


if __name__ == '__main__':
    unittest.main()
