from settings import PLAYER1, PLAYER2


class TRUN_CONTROLLER:
    def __init__(self):
        self.now = PLAYER1

    def next(self):
        self.now = PLAYER2 if self.now == PLAYER1 else PLAYER1

    def get(self):
        return self.now


class GAME_CONTROLLER:
    def __init__(self, board, board_drawer, board_controller):
        self.board = board
        self.board_drawer = board_drawer
        self.board_controller = board_controller
        self.teban = TRUN_CONTROLLER()

    def proceed(self, pos):
        can_update_board = self.board_controller.can_update_board(pos, self.teban.get())
        if not can_update_board:
            raise Exception("返せるピースなし")
        self.board_controller.update_board(pos, self.teban.get())
        self.teban.next()
        self.board_drawer.draw(self.board)
