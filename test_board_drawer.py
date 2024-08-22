import unittest
from unittest.mock import Mock
from board import BOARD
from board_drawer import BOARD_DRAWER


class TestBOARD_DRAWER(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()
        self.canvas = Mock()
        self.board_drawer = BOARD_DRAWER(self.canvas)

    def test_draw(self):
        self.board_drawer.draw(self.board)
        self.assertEqual(self.canvas.create_rectangle.call_count, 64)
        self.assertEqual(self.canvas.create_oval.call_count, 4)


if __name__ == "__main__":
    unittest.main()
