import unittest
from board import BOARD
from settings import BLACK, WHITE


class TestBOARD(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()

    def test_initial_board_setup(self):
        self.assertEqual(self.board.get_color((3, 3)), BLACK)
        self.assertEqual(self.board.get_color((4, 4)), BLACK)
        self.assertEqual(self.board.get_color((3, 4)), WHITE)
        self.assertEqual(self.board.get_color((4, 3)), WHITE)

    def test_set_color_valid(self):
        self.board.set_color((0, 0), BLACK)
        self.assertEqual(self.board.get_color((0, 0)), BLACK)

    def test_set_color_invalid_pos(self):
        with self.assertRaises(Exception) as context:
            self.board.set_color((8, 8), BLACK)
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
