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
    BOARD_LEN = 8

    def __init__(self):
        self.board = []
        for r in range(self.BOARD_LEN):
            column = []
            for c in range(self.BOARD_LEN):
                column.append(PIECE())
            self.board.append(column)
        self._initialize()

    def _initialize(self):
        half = int(self.BOARD_LEN / 2)

        self.set_status((half - 1, half), PLAYER1)
        self.set_status((half, half - 1), PLAYER1)
        self.set_status((half, half), PLAYER2)
        self.set_status((half - 1, half - 1), PLAYER2)

    def _get_piece(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.board[pos[0]][pos[1]]

    def is_valid_pos(self, pos):
        return ((0 <= pos[0]) and (pos[0] < self.BOARD_LEN)) and (
            (0 <= pos[1]) and (pos[1] < self.BOARD_LEN)
        )

    def set_status(self, pos, color):
        self._get_piece(pos).set_status(color)

    def turn_status(self, pos):
        self._get_piece(pos).turn_status()

    def get_status(self, pos):
        return self._get_piece(pos).get_status()

    def get_side_len(self):
        return self.BOARD_LEN

    def is_empty(self, pos):
        return self.get_status(pos) == EMPTY
