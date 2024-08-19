import tkinter

WINDOW_WIDTH = 528
WINDOW_HEIGHT = 528

BOARD_BEGIN_OFFSET = 72
CELL_LEN = 48

GREEN = "GREEN"
BLACK = "BLACK"
WHITE = "WHITE"


class Koma:
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


class BORAD:
    BOARD_LEN = 8

    def __init__(self):
        self.board = []
        for i in range(self.BOARD_LEN**2):
            self.board.append(Koma())
        self.initialize()

    def initialize(self):
        # ここ上手いこと置き換え
        self.set_color(27, BLACK)
        self.set_color(28, WHITE)
        self.set_color(36, BLACK)
        self.set_color(35, WHITE)

    def set_color(self, pos_1d, color):
        self.board[pos_1d].set_color(color)

    def turn_color(self, pos_1d):
        self.board[pos_1d].turn_color()

    def get_color(self, pos_1d):
        return self.board[pos_1d].get_color()

    def get_side_len(self):
        return self.BOARD_LEN

    def convert_index_2d_1d(self, pos_2d):
        return pos_2d[1] * self.BOARD_LEN + pos_2d[0]

    def convert_index_1d_2d(self, pos_1d):
        return (pos_1d % self.BOARD_LEN, pos_1d // self.BOARD_LEN)

    def change_color(self, pos_2d):
        pos_1d = self.convert_index_2d_1d(pos_2d)
        if self.get_color(pos_1d) == GREEN:
            self.set_color(pos_1d, BLACK)
        else:
            self.turn_color(pos_1d)


class BORAD_UI:
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
                fill=board.get_color(i),
                width=2,
            )

    def pos_convert(self, pos):
        if (pos[0] < BOARD_BEGIN_OFFSET) or (
            pos[0] > WINDOW_WIDTH - BOARD_BEGIN_OFFSET
        ):
            raise Exception("範囲外")
        if (pos[1] < BOARD_BEGIN_OFFSET) or (
            pos[1] > WINDOW_HEIGHT - BOARD_BEGIN_OFFSET
        ):
            raise Exception("範囲外")

        return (
            int((pos[0] - BOARD_BEGIN_OFFSET) / CELL_LEN),
            int((pos[1] - BOARD_BEGIN_OFFSET) / CELL_LEN),
        )


class GAME_CONTROLLER:
    def __init__(self, board_ui, board, canvas):
        self.board_ui = board_ui
        self.board = board
        self.canvas = canvas

    def click_event(self, click_event):
        board_pos = self.board_ui.pos_convert((click_event.x, click_event.y))
        self.board.change_color(board_pos)
        self.update()

    def update(self):
        self.board_ui.draw_board(self.board, self.canvas)


# ルート画面の作成
root = tkinter.Tk()
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

# キャンバスウィジェットの配置
canvas = tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
canvas.pack()

# ボードの描画
board = BORAD()
board_ui = BORAD_UI(BOARD_BEGIN_OFFSET, CELL_LEN)
game_controller = GAME_CONTROLLER(board_ui, board, canvas)
game_controller.update()

canvas.bind("<Button-1>", game_controller.click_event)
# 実行
root.mainloop()
