from settings import GREEN, BLACK, WHITE


class PIECE:
    COLOR_SET = {GREEN, BLACK, WHITE}

    def __init__(self):
        self.color = GREEN

    def set_color(self, color):
        if color in self.COLOR_SET:
            self.color = color
        else:
            raise Exception("設定可能値以外")

    def turn_color(self):
        if self.color == GREEN:
            raise Exception("反転不可")
        self.color = WHITE if self.color == BLACK else BLACK

    def get_color(self):
        return self.color


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

        self.set_color((half, half), BLACK)
        self.set_color((half - 1, half - 1), BLACK)
        self.set_color((half - 1, half), WHITE)
        self.set_color((half, half - 1), WHITE)

    def set_color(self, pos, color):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        self.get_piece(pos).set_color(color)

    def turn_color(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        self.get_piece(pos).turn_color()

    def get_color(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.get_piece(pos).get_color()

    def get_side_len(self):
        return self.BOARD_LEN

    def get_piece(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.board[pos[0]][pos[1]]

    def is_empty(self, pos):
        if not self.is_valid_pos(pos):
            raise Exception("範囲外")
        return self.get_color(pos) == GREEN
