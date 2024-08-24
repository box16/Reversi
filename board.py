from settings import EMPTY, PLAYER1, PLAYER2


class PIECE:
    def __init__(self):
        self.status = EMPTY

    def set(self, status):
        if status in {PLAYER1, PLAYER2}:
            self.status = status
        else:
            raise Exception("設定可能値以外")

    def turn(self):
        if self.status == EMPTY:
            raise Exception("反転不可")
        self.status = PLAYER2 if self.status == PLAYER1 else PLAYER1

    def get(self):
        return self.status

    def reset(self):
        self.status = EMPTY

    def is_empty(self):
        return self.status == EMPTY


class BOARD:
    BOARD_LEN = 8

    def __init__(self):
        self.board = [
            [PIECE() for j in range(self.BOARD_LEN)] for i in range(self.BOARD_LEN)
        ]

        half = int(self.BOARD_LEN / 2)
        self.set((half - 1, half), PLAYER1)
        self.set((half, half - 1), PLAYER1)
        self.set((half, half), PLAYER2)
        self.set((half - 1, half - 1), PLAYER2)

    def _get_piece(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.board[pos[0]][pos[1]]

    def is_valid_pos(self, pos):
        return ((0 <= pos[0]) and (pos[0] < self.BOARD_LEN)) and (
            (0 <= pos[1]) and (pos[1] < self.BOARD_LEN)
        )

    def get_side_len(self):
        return self.BOARD_LEN

    def set(self, pos, player):
        self._get_piece(pos).set(player)

    def turn(self, pos):
        self._get_piece(pos).turn()

    def get(self, pos):
        return self._get_piece(pos).get()

    def reset(self, pos):
        return self._get_piece(pos).reset()

    def is_empty(self, pos):
        return self._get_piece(pos).is_empty()

    def count(self, player):
        num = 0
        for row in self.board:
            for piece in row:
                if piece.get() == player:
                    num += 1
        return num
