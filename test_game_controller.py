import unittest
from board import BOARD
from board_checker import BOARD_CHECKER
from game_controller import GAME_CONTROLLER
from settings import PLAYER1, PLAYER2


class TestGameController(unittest.TestCase):

    def setUp(self):
        self.board = BOARD()
        self.mock_board_drawer = MockBoardDrawer()
        self.board_checker = BOARD_CHECKER()
        self.mock_turn_label = MockTurnLabel()

        self.game_controller = GAME_CONTROLLER(
            self.board, self.mock_board_drawer, self.board_checker, self.mock_turn_label
        )

    def test_prepare_initial_state(self):
        # テストケース 1: 初期状態での盤面の準備
        self.game_controller.prepare()
        self.assertEqual(
            self.mock_turn_label.text, f"Next : {self.game_controller.turn.get()}"
        )
        self.assertTrue(self.mock_board_drawer.draw_called)
        self.assertEqual(self.mock_board_drawer.board_state, self.board)

    def test_proceed_valid_position(self):
        # テストケース 2: 配置可能な位置での進行
        place_pos = (2, 3)
        turn_pos = (3, 3)
        self.game_controller.prepare()
        self.game_controller.proceed(place_pos)

        self.assertEqual(self.board.get(place_pos), PLAYER1)
        self.assertEqual(self.board.get(turn_pos), PLAYER1)

    def test_proceed_invalid_position(self):
        # テストケース 3: 配置不可能な位置での進行
        place_pos = [(3, 3), (4, 3), (5, 3), (7, 3)]
        self.game_controller.prepare()

        with self.assertRaises(Exception) as context:
            for pos in place_pos:
                self.game_controller.proceed(pos)
        self.assertTrue("配置可能位置でない" in str(context.exception))

    def test_skip_turn_when_no_available_moves(self):
        # テストケース 4: 配置可能な位置がない場合のスキップ(黒の最短パスパターン)
        self.game_controller.prepare()
        place_pos = [
            (5, 4),  # P1
            (5, 5),  # P2
            (3, 2),  # P1
            (6, 4),  # P2
            (7, 4),  # P1
            (7, 3),  # P2
            (5, 6),  # P1
            (7, 5),
        ]  # P2
        for pos in place_pos:
            self.game_controller.proceed(pos)
        self.assertTrue(PLAYER2 in self.mock_turn_label.text)
        self.assertEqual(self.game_controller.turn.get(), PLAYER2)

    def test_game_end(self):
        # テストケース 5: ゲーム終了の判定(黒の最短全滅パターン)
        self.game_controller.prepare()
        place_pos = [
            (5, 4),
            (3, 5),
            (2, 4),
            (5, 3),
            (4, 6),
            (5, 5),
            (6, 4),
            (4, 5),
            (4, 2),
        ]
        for pos in place_pos:
            self.game_controller.proceed(pos)
        self.assertTrue(self.game_controller.is_end)
        self.assertTrue("Game Is End." in self.mock_turn_label.text)


class MockBoardDrawer:
    def __init__(self):
        self.draw_called = False
        self.board_state = None

    def draw(self, board):
        self.draw_called = True
        self.board_state = board


class MockTurnLabel:
    def __init__(self):
        self.text = ""

    def config(self, text):
        self.text = text


if __name__ == "__main__":
    unittest.main()
