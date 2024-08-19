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
    BOARD_LEN = 8  # 偶数を想定

    def __init__(self):
        self.board = []
        for i in range(self.BOARD_LEN):
            column = []
            for j in range(self.BOARD_LEN):
                column.append(Koma())
            self.board.append(column)
        self.initialize()

    def initialize(self):
        half = int(self.BOARD_LEN / 2)

        self.set_color((half - 1, half - 1), BLACK)
        self.set_color((half - 1, half), WHITE)
        self.set_color((half, half), BLACK)
        self.set_color((half, half - 1), WHITE)

    def set_color(self, pos, color):
        self.get_koma(pos).set_color(color)

    def turn_color(self, pos):
        self.get_koma(pos).turn_color()

    def get_color(self, pos):
        return self.get_koma(pos).get_color()

    def get_side_len(self):
        return self.BOARD_LEN

    def can_click(self, pos):
        return self.get_color(pos) == GREEN

    def get_koma(self, pos):
        return self.board[pos[0]][pos[1]]


class BORAD_UI:
    def __init__(self, offset, cell_len):
        self.offset = offset
        self.cell_len = cell_len

    def draw_board(self, board, canvas):
        for i in range(board.get_side_len()):
            for j in range(board.get_side_len()):
                begin = (
                    self.offset + i * self.cell_len,
                    self.offset + j * self.cell_len,
                )

                canvas.create_rectangle(
                    begin[0],
                    begin[1],
                    begin[0] + self.cell_len,
                    begin[1] + self.cell_len,
                    fill=GREEN,
                    width=2,
                )
                if board.get_color((i, j)) == GREEN:
                    continue
                else:
                    r = self.cell_len / 10
                    canvas.create_oval(
                        begin[0] + r,
                        begin[1] + r,
                        begin[0] + self.cell_len - r,
                        begin[1] + self.cell_len - r,
                        fill=board.get_color((i, j)),
                        width=2,
                    )

    def to_board_pos(self, pos):
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
        board_pos = self.board_ui.to_board_pos((click_event.x, click_event.y))
        if self.board.can_click(board_pos):
            self.board.set_color(board_pos, BLACK)
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
