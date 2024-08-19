import unittest
from settings import GREEN, BLACK, WHITE
from piece import PIECE


class TestPIECE(unittest.TestCase):
    def test_initial_color(self):
        piece = PIECE()
        self.assertEqual(piece.get_color(), GREEN)

    def test_set_color(self):
        piece = PIECE()
        piece.set_color(BLACK)
        self.assertEqual(piece.get_color(), BLACK)
        piece.set_color(WHITE)
        self.assertEqual(piece.get_color(), WHITE)

    def test_set_invalid_color(self):
        piece = PIECE()
        with self.assertRaises(Exception) as context:
            piece.set_color("INVALID_COLOR")
        self.assertTrue("設定可能値以外" in str(context.exception))

    def test_turn_color(self):
        piece = PIECE()
        piece.set_color(BLACK)
        piece.turn_color()
        self.assertEqual(piece.get_color(), WHITE)
        piece.turn_color()
        self.assertEqual(piece.get_color(), BLACK)

    def test_turn_color_invalid(self):
        piece = PIECE()
        with self.assertRaises(Exception) as context:
            piece.turn_color()
        self.assertTrue("反転不可" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
