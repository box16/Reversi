import unittest
from settings import PLAYER1
from board import BOARD
from board_checker import BOARD_CHECKER


class TestBOARD_CHECKER(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()
        self.rule = BOARD_CHECKER()

    def test_no_get_turn_pieces(self):
        pos = (0, 0)
        can_turn_piece = self.rule.get_turn_pieces(self.board, pos, PLAYER1)
        self.assertEqual(can_turn_piece, [])

    def test_get_turn_pieces(self):
        pos = (3, 2)
        can_turn_piece = self.rule.get_turn_pieces(self.board, pos, PLAYER1)
        self.assertEqual(can_turn_piece, [(3, 3)])

    def test_invalid_position(self):
        with self.assertRaises(Exception):
            self.rule.get_turn_pieces(self.board, (8, 8), PLAYER1)


if __name__ == "__main__":
    unittest.main()
