import unittest
from board import BOARD, PIECE
from settings import EMPTY, PLAYER1, PLAYER2


class TestPIECE(unittest.TestCase):
    def test_initial_color(self):
        piece = PIECE()
        self.assertEqual(piece.get_color(), EMPTY)

    def test_set_color(self):
        piece = PIECE()
        piece.set_color(PLAYER1)
        self.assertEqual(piece.get_color(), PLAYER1)
        piece.set_color(PLAYER2)
        self.assertEqual(piece.get_color(), PLAYER2)

    def test_set_invalid_color(self):
        piece = PIECE()
        with self.assertRaises(Exception) as context:
            piece.set_color("INVALID_COLOR")
        self.assertTrue("設定可能値以外" in str(context.exception))

    def test_turn_color(self):
        piece = PIECE()
        piece.set_color(PLAYER1)
        piece.turn_color()
        self.assertEqual(piece.get_color(), PLAYER2)
        piece.turn_color()
        self.assertEqual(piece.get_color(), PLAYER1)

    def test_turn_color_invalid(self):
        piece = PIECE()
        with self.assertRaises(Exception) as context:
            piece.turn_color()
        self.assertTrue("反転不可" in str(context.exception))


class TestBOARD(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()

    def test_initial_board_setup(self):
        self.assertEqual(self.board.get_color((3, 3)), PLAYER1)
        self.assertEqual(self.board.get_color((4, 4)), PLAYER1)
        self.assertEqual(self.board.get_color((3, 4)), PLAYER2)
        self.assertEqual(self.board.get_color((4, 3)), PLAYER2)

    def test_set_color_valid(self):
        self.board.set_color((0, 0), PLAYER1)
        self.assertEqual(self.board.get_color((0, 0)), PLAYER1)

    def test_set_color_invalid_pos(self):
        with self.assertRaises(Exception) as context:
            self.board.set_color((8, 8), PLAYER1)
        self.assertTrue("範囲外" in str(context.exception))

    def test_get_color_invalid_pos(self):
        with self.assertRaises(Exception) as context:
            self.board.get_color((8, 8))
        self.assertTrue("範囲外" in str(context.exception))

    def test_is_empty(self):
        self.assertTrue(self.board.is_empty((0, 0)))
        self.assertFalse(self.board.is_empty((3, 3)))


if __name__ == "__main__":
    unittest.main()
