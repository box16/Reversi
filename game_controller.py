from settings import BOARD_DRAW_OFFSET, CELL_SIZE
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from settings import PLAYER1, PLAYER2
from board_checker import BOARD_CHECKER


class TRUN_CONTROLLER:
    def __init__(self):
        self.now = PLAYER1

    def next(self):
        self.now = PLAYER2 if self.now == PLAYER1 else PLAYER1

    def get(self):
        return self.now


class GAME_CONTROLLER:
    def __init__(self, board_drawer, board):
        self.board_drawer = board_drawer
        self.board = board
        self.teban = TRUN_CONTROLLER()

        # ここリファクタ
        self.rule = BOARD_CHECKER()

    def click_event(self, click_event):
        board_pos = self.to_board_pos((click_event.x, click_event.y))

        change_pos = self.rule.get_turn_pieces(self.board, board_pos, self.teban.get())
        if not change_pos:
            raise Exception("チェック通らず")

        self.board.set_status(board_pos, self.teban.get())
        for pos in change_pos:
            self.board.turn_status(pos)
        self.teban.next()
        self.update()

    def update(self):
        self.board_drawer.draw()

    def to_board_pos(self, pos):
        if (pos[0] < BOARD_DRAW_OFFSET) or (pos[0] > WINDOW_WIDTH - BOARD_DRAW_OFFSET):
            raise Exception("範囲外")
        if (pos[1] < BOARD_DRAW_OFFSET) or (pos[1] > WINDOW_HEIGHT - BOARD_DRAW_OFFSET):
            raise Exception("範囲外")

        return (
            int((pos[0] - BOARD_DRAW_OFFSET) / CELL_SIZE),
            int((pos[1] - BOARD_DRAW_OFFSET) / CELL_SIZE),
        )
