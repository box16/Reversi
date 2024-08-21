import unittest
from settings import PLAYER1
from board import BOARD
from board_checker import BOARD_CHECKER


class TestBOARD_CHECKER(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()
        self.board_checker = BOARD_CHECKER(self.board)

    def test_no_get_turn_pieces(self):
        pos = (0, 0)
        can_turn_piece = self.board_checker.get_turn_pieces(pos, PLAYER1)
        self.assertEqual(can_turn_piece, [])

    def test_get_turn_pieces(self):
        pos = (3, 2)
        can_turn_piece = self.board_checker.get_turn_pieces(pos, PLAYER1)
        self.assertEqual(can_turn_piece, [(3, 3)])

    def test_invalid_position(self):
        with self.assertRaises(Exception):
            self.board_checker.get_turn_pieces((8, 8), PLAYER1)


if __name__ == "__main__":
    unittest.main()
