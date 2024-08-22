import unittest
from board import BOARD, PIECE
from settings import EMPTY, PLAYER1, PLAYER2


class TestPIECE(unittest.TestCase):
    # 初期値はEMPTY
    def test_initial_status(self):
        piece = PIECE()
        self.assertEqual(piece.get(), EMPTY)

    # status設定を指定できる
    def test_set_status(self):
        piece = PIECE()
        piece.set(PLAYER1)
        self.assertEqual(piece.get(), PLAYER1)
        piece.set(PLAYER2)
        self.assertEqual(piece.get(), PLAYER2)

    # 想定外のstatusで例外
    def test_set_invalid_status(self):
        piece = PIECE()
        with self.assertRaises(Exception) as context:
            piece.set("INVALID_COLOR")
        self.assertTrue("設定可能値以外" in str(context.exception))

    # PLAYER1,PLAYER2は反転可能
    def test_turn_status(self):
        piece = PIECE()
        piece.set(PLAYER1)
        piece.turn()
        self.assertEqual(piece.get(), PLAYER2)
        piece.turn()
        self.assertEqual(piece.get(), PLAYER1)

    # EMPTYで反転はできない
    def test_turn_status_invalid(self):
        piece = PIECE()
        with self.assertRaises(Exception) as context:
            piece.turn()
        self.assertTrue("反転不可" in str(context.exception))

    # resetでEMPTY
    def test_reset_status(self):
        piece = PIECE()
        piece.set(PLAYER1)
        piece.reset()
        self.assertEqual(piece.get(), EMPTY)

    # emptyチェック
    def test_is_empty(self):
        piece = PIECE()
        self.assertTrue(piece.is_empty())
        piece.set(PLAYER1)
        self.assertFalse(piece.is_empty())


class TestBOARD(unittest.TestCase):
    def setUp(self):
        self.board = BOARD()

    # 黒・白の初期配置テスト
    def test_initial_board_setup(self):
        self.assertEqual(self.board.get((3, 4)), PLAYER1)
        self.assertEqual(self.board.get((4, 3)), PLAYER1)
        self.assertEqual(self.board.get((3, 3)), PLAYER2)
        self.assertEqual(self.board.get((4, 4)), PLAYER2)

    # 指定した位置に指定したstatusを設定できる
    def test_set_status_valid(self):
        self.board.set((0, 0), PLAYER1)
        self.assertEqual(self.board.get((0, 0)), PLAYER1)
        self.board.set((1, 1), PLAYER2)
        self.assertEqual(self.board.get((1, 1)), PLAYER2)

    # 範囲外に配置はできない
    def test_set_status_invalid_pos(self):
        side_len = self.board.get_side_len()
        with self.assertRaises(Exception) as context:
            self.board.set((side_len, side_len), PLAYER1)
        self.assertTrue("範囲外" in str(context.exception))

    # 範囲外の値は取得できない
    def test_get_status_invalid_pos(self):
        side_len = self.board.get_side_len()
        with self.assertRaises(Exception) as context:
            self.board.get((side_len, side_len))
        self.assertTrue("範囲外" in str(context.exception))

    # 空チェック
    def test_is_empty(self):
        self.assertTrue(self.board.is_empty((0, 0)))
        self.assertFalse(self.board.is_empty((3, 3)))

    # 指定した位置を反転できる
    def test_initial_board_setup(self):
        self.assertEqual(self.board.get((3, 4)), PLAYER1)
        self.board.turn((3, 4))
        self.assertEqual(self.board.get((3, 4)), PLAYER2)


if __name__ == "__main__":
    unittest.main()
