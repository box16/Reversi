from settings import PLAYER1, PLAYER2


class TURN_CONTROLLER:
    def __init__(self):
        self.now = PLAYER1

    def next(self):
        self.now = PLAYER2 if self.now == PLAYER1 else PLAYER1

    def get(self):
        return self.now


class GAME_CONTROLLER:
    def __init__(self, board, board_drawer, board_checker, turn_label):
        self.board = board
        self.board_drawer = board_drawer
        self.board_checker = board_checker
        self.turn = TURN_CONTROLLER()
        self.turn_label = turn_label

    def prepare(self):
        self.board_drawer.draw(self.board)
        self.turn_label.config(text=f"Next : {self.turn.get()}")
        # 終了チェックをここに入れる
        self.can_place_pos = self.board_checker.get_can_place_pos(
            self.board, self.turn.get()
        )

    def proceed(self, pos):
        if pos not in self.can_place_pos:
            raise Exception("配置可能位置でない")
        self.board.set(pos, self.turn.get())
        for p in self.can_place_pos[pos]:
            self.board.turn(p)
        self.turn.next()
        self.prepare()
