import unittest
from unittest.mock import Mock
from board import BOARD
from board_ui import BOARD_UI
from settings import CELL_LEN
from settings import BOARD_BEGIN_OFFSET


class TestBOARD_UI(unittest.TestCase):
    def setUp(self):
        self.board_ui = BOARD_UI(BOARD_BEGIN_OFFSET, CELL_LEN)
        self.board = BOARD()
        self.canvas = Mock()

    def test_draw_board(self):
        self.board_ui.draw_board(self.board, self.canvas)
        self.assertEqual(self.canvas.create_rectangle.call_count, 64)  # 8x8 squares
        self.assertEqual(self.canvas.create_oval.call_count, 4)  # 4 initial pieces

    def test_to_board_pos_valid(self):
        pos = (100, 100)
        board_pos = self.board_ui.to_board_pos(pos)
        self.assertEqual(board_pos, (0, 0))

    def test_to_board_pos_invalid(self):
        pos = (50, 50)  # Outside the valid board area
        with self.assertRaises(Exception) as context:
            self.board_ui.to_board_pos(pos)
        self.assertTrue("範囲外" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
