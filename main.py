import tkinter
from settings import PLAYER1, PLAYER2
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from settings import BOARD_DRAW_OFFSET, CELL_SIZE
from board import BOARD
from board_drawer import BOARD_DRAWER
from rule import PIECE_ARE_NEARBY


class TEBAN_CONTROLLER:
    def __init__(self):
        self.now = PLAYER1

    def next(self):
        self.now = PLAYER2 if self.now == PLAYER1 else PLAYER1

    def get(self):
        return self.now


class GAME_CONTROLLER:
    def __init__(self, board_drawer, board, canvas, teban):
        self.board_drawer = board_drawer
        self.board = board
        self.canvas = canvas
        self.teban = teban

        # ここリファクタ
        self.rule = PIECE_ARE_NEARBY()

    def click_event(self, click_event):
        board_pos = self.to_board_pos((click_event.x, click_event.y))

        change_pos = self.rule.check(self.board, board_pos, self.teban.get())
        if not change_pos:
            raise Exception("チェック通らず")

        self.board.set_status(board_pos, self.teban.get())
        for pos in change_pos:
            self.board.turn_status(pos)
        self.teban.next()
        self.update()

    def update(self):
        self.board_drawer.draw()

    def to_board_pos(self, pos):
        if (pos[0] < BOARD_DRAW_OFFSET) or (pos[0] > WINDOW_WIDTH - BOARD_DRAW_OFFSET):
            raise Exception("範囲外")
        if (pos[1] < BOARD_DRAW_OFFSET) or (pos[1] > WINDOW_HEIGHT - BOARD_DRAW_OFFSET):
            raise Exception("範囲外")

        return (
            int((pos[0] - BOARD_DRAW_OFFSET) / CELL_SIZE),
            int((pos[1] - BOARD_DRAW_OFFSET) / CELL_SIZE),
        )


if __name__ == "__main__":
    # ルート画面の作成
    root = tkinter.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # キャンバスウィジェットの配置
    canvas = tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    # ボードの描画
    board = BOARD()
    board_drawer = BOARD_DRAWER(board, canvas)

    teban = TEBAN_CONTROLLER()

    game_controller = GAME_CONTROLLER(board_drawer, board, canvas, teban)
    game_controller.update()

    canvas.bind("<Button-1>", game_controller.click_event)
    # 実行
    root.mainloop()
