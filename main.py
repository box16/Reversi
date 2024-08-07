import tkinter

WINDOW_WIDTH = 528
WINDOW_HEIGHT = 528

BOARD_BEGIN_OFFSET = 72
CELL_LEN = 48

GREEN = 255
BLACK = 0
WHITE = 1


class BORAD:
    BOARD_LEN = 8

    def __init__(self):
        self.board = bytearray(self.BOARD_LEN**2)
        self.initialize()

    def initialize(self):
        for i in range(self.BOARD_LEN**2):
            self.set_color(i, GREEN)
        self.set_color(27, BLACK)
        self.set_color(28, WHITE)
        self.set_color(36, BLACK)
        self.set_color(35, WHITE)

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
        return self.BOARD_LEN

    def convert_index_2d_1d(self, pos):
        return pos[1] * self.BOARD_LEN + pos[0]

    def convert_index_1d_2d(self, pos):
        return (pos % self.BOARD_LEN, pos // self.BOARD_LEN)


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
                fill="Green",
                width=2,
            )
            if board.get_color(i) == GREEN:
                continue

            r = self.cell_len / 10
            canvas.create_oval(
                begin[0] + r,
                begin[1] + r,
                begin[0] + self.cell_len - r,
                begin[1] + self.cell_len - r,
                fill=board.get_color_str(i),
                width=2,
            )


def canvas_click(click_event):
    if (click_event.x < BOARD_BEGIN_OFFSET) or (
        click_event.x > WINDOW_WIDTH - BOARD_BEGIN_OFFSET
    ):
        return
    if (click_event.y < BOARD_BEGIN_OFFSET) or (
        click_event.y > WINDOW_HEIGHT - BOARD_BEGIN_OFFSET
    ):
        return

    click_pos = (
        int((click_event.x - BOARD_BEGIN_OFFSET) / CELL_LEN),
        int((click_event.y - BOARD_BEGIN_OFFSET) / CELL_LEN),
    )
    click_pos = board.convert_index_2d_1d(click_pos)

    board.set_color(click_pos, BLACK)
    drawer.draw_board(board, canvas)


# ルート画面の作成
root = tkinter.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# キャンバスウィジェットの配置
canvas = tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# ボードの描画
board = BORAD()
drawer = BORAD_DRAWER(BOARD_BEGIN_OFFSET, CELL_LEN)
drawer.draw_board(board, canvas)

canvas.bind("<Button-1>", canvas_click)
# 実行
root.mainloop()
