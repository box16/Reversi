import unittest
from settings import PLAYER1, PLAYER2
from board import BOARD
from board_checker import BOARD_CHECKER


class TestBOARD_CHECKER(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()
        self.board_checker = BOARD_CHECKER()

    def test_get_can_place_info(self):
        can_place_info = self.board_checker.get_can_place_pos(self.board, PLAYER1)
        expect = {
            (2, 3): [(3, 3)],
            (3, 2): [(3, 3)],
            (4, 5): [(4, 4)],
            (5, 4): [(4, 4)],
        }
        self.assertEqual(can_place_info, expect)

    def test_get_can_place_pos_empty(self):
        for i in range(self.board.get_side_len()):
            for j in range(self.board.get_side_len()):
                self.board.set((i, j), PLAYER2)
        can_place_info = self.board_checker.get_can_place_pos(self.board, PLAYER1)
        self.assertEqual(can_place_info, {})


if __name__ == "__main__":
    unittest.main()
