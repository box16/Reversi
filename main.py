import tkinter
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from board import BOARD
from board_drawer import BOARD_DRAWER
from game_controller import GAME_CONTROLLER

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

    game_controller = GAME_CONTROLLER(board_drawer, board)
    game_controller.update()

    # これどこかに
    canvas.bind("<Button-1>", game_controller.click_event)
    # 実行
    root.mainloop()
