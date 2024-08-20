import unittest
from settings import PLAYER1
from board import BOARD
from rule import PIECE_ARE_NEARBY


class TestPIECE_ARE_NEARBY(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()
        self.rule = PIECE_ARE_NEARBY()

    def test_no_pieces_nearby(self):
        pos = (0, 0)
        can_turn_piece = self.rule.check(self.board, pos, PLAYER1)
        self.assertEqual(can_turn_piece, [])

    def test_pieces_nearby(self):
        pos = (4, 2)
        can_turn_piece = self.rule.check(self.board, pos, PLAYER1)
        self.assertEqual(can_turn_piece, [(4, 3)])

    def test_invalid_position(self):
        with self.assertRaises(Exception):
            self.rule.check(self.board, (8, 8), PLAYER1)


if __name__ == "__main__":
    unittest.main()
