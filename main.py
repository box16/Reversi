import tkinter

WINDOW_WIDTH = 528
WINDOW_HEIGHT = 528

BOARD_LEN = 8
CELL_LEN = 48
BOARD_BEGIN_OFFSET = 72

GREEN = 255
BLACK = 0
WHITE = 1


class BORAD:
    def __init__(self, side_len):
        self.side_len = side_len
        self.board = bytearray(self.side_len**2)
        self.initialize()

    def initialize(self):
        for i in range(self.side_len**2):
            self.set_color(i, GREEN)

    def set_color(self, pos, color):
        self.board[pos] = color

    def get_color(self, pos):
        return self.board[pos]

    def get_color_str(self, pos):
        if self.board[pos] == GREEN:
            return "Green"
        elif self.board[pos] == BLACK:
            return "Black"
        else:
            return "White"

    def get_side_len(self):
        return self.side_len

    def convert_index_2d_1d(self, pos):
        return pos[1] * self.side_len + pos[0]

    def convert_index_1d_2d(self, pos):
        return (pos % self.side_len, pos // self.side_len)


class BORAD_DRAWER:
    def __init__(self, offset, cell_len):
        self.offset = offset
        self.cell_len = cell_len

    def draw_board(self, board, canvas):
        for i in range(board.get_side_len() ** 2):
            pos = board.convert_index_1d_2d(i)
            begin = (
                self.offset + pos[0] * self.cell_len,
                self.offset + pos[1] * self.cell_len,
            )

            canvas.create_rectangle(
                begin[0],
                begin[1],
                begin[0] + self.cell_len,
                begin[1] + self.cell_len,
                fill=board.get_color_str(i),
                width=2,
            )


# ルート画面の作成
root = tkinter.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# キャンバスウィジェットの配置
canvas = tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# ボードの描画
board = BORAD(BOARD_LEN)
drawer = BORAD_DRAWER(BOARD_BEGIN_OFFSET, CELL_LEN)
drawer.draw_board(board, canvas)

# 実行
root.mainloop()
