from settings import EMPTY, PLAYER1, PLAYER2


class PIECE:
    def __init__(self):
        self.status = EMPTY

    def set_status(self, status):
        if status in {PLAYER1, PLAYER2}:
            self.status = status
        else:
            raise Exception("設定可能値以外")

    def turn_status(self):
        if self.status == EMPTY:
            raise Exception("反転不可")
        self.status = PLAYER2 if self.status == PLAYER1 else PLAYER1

    def get_status(self):
        return self.status

    def reset_status(self):
        self.status = EMPTY


class BOARD:
    BOARD_LEN = 8  # 偶数を想定

    def __init__(self):
        self.board = []
        for i in range(self.BOARD_LEN):
            column = []
            for j in range(self.BOARD_LEN):
                column.append(PIECE())
            self.board.append(column)
        self.initialize()

    def is_valid_pos(self, pos):
        return ((0 <= pos[0]) and (pos[0] < self.BOARD_LEN)) and (
            (0 <= pos[1]) and (pos[1] < self.BOARD_LEN)
        )

    def initialize(self):
        half = int(self.BOARD_LEN / 2)

        self.set_status((half, half), PLAYER1)
        self.set_status((half - 1, half - 1), PLAYER1)
        self.set_status((half - 1, half), PLAYER2)
        self.set_status((half, half - 1), PLAYER2)

    def set_status(self, pos, color):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        self.get_piece(pos).set_status(color)

    def turn_status(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        self.get_piece(pos).turn_status()

    def get_status(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.get_piece(pos).get_status()

    def get_side_len(self):
        return self.BOARD_LEN

    def get_piece(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.board[pos[0]][pos[1]]

    def is_empty(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.get_status(pos) == EMPTY
