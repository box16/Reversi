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
        self.is_end_pre = False
        self.is_end = False

    def prepare(self):
        self.can_place_pos = self.board_checker.get_can_place_pos(
            self.board, self.turn.get()
        )
        self.turn_label.config(text=f"Next : {self.turn.get()}")
        self.board_drawer.draw(self.board)

        if not self.can_place_pos:
            if self.is_end_pre:
                self.is_end = True
                self.end()
                return
            else:
                self.is_end_pre = True
                self.turn.next()
                self.prepare()
                return
        self.is_end_pre = False

    def proceed(self, pos):
        if pos not in self.can_place_pos:
            raise Exception("配置可能位置でない")
        self.board.set(pos, self.turn.get())
        for p in self.can_place_pos[pos]:
            self.board.turn(p)
        self.turn.next()
        self.prepare()

    def end(self):
        player_1_num = self.board.count(PLAYER1)
        player_2_num = self.board.count(PLAYER2)
        self.turn_label.config(
            text=f"Game Is End.\n {PLAYER1} : {player_1_num} {PLAYER2} : {player_2_num} "
        )
