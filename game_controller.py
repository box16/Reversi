from settings import PLAYER1, PLAYER2


class TRUN_CONTROLLER:
    def __init__(self):
        self.now = PLAYER1

    def next(self):
        self.now = PLAYER2 if self.now == PLAYER1 else PLAYER1

    def get(self):
        return self.now


class GAME_CONTROLLER:
    def __init__(self, board, board_drawer, board_controller, canvas):
        self.board = board
        self.board_drawer = board_drawer
        self.board_controller = board_controller
        self.teban = TRUN_CONTROLLER()
        canvas.bind("<Button-1>", self.click_event)

    def click_event(self, click_event):
        pos = self.board_drawer.convert_board_pos((click_event.x, click_event.y))
        can_update_board = self.board_controller.can_update_board(pos, self.teban.get())
        if not can_update_board:
            raise Exception("返せるピースなし")
        self.board_controller.update_board(pos, self.teban.get())
        self.teban.next()
        self.update()

    def update(self):
        self.board_drawer.draw(self.board)
