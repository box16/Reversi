import unittest
from unittest.mock import Mock
from board import BOARD
from board_ui_controller import BOARD_UI_CONTROLLER


class TestBOARD_UI_CONTROLLER(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()
        self.canvas = Mock()
        self.board_ui_controller = BOARD_UI_CONTROLLER(self.board, self.canvas)

    def test_draw_board(self):
        self.board_ui_controller.draw()
        self.assertEqual(self.canvas.create_rectangle.call_count, 64)  # 8x8 squares
        self.assertEqual(self.canvas.create_oval.call_count, 4)  # 4 initial pieces


if __name__ == "__main__":
    unittest.main()
