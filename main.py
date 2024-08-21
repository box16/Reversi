import tkinter
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from board import BOARD
from board_ui_controller import BOARD_UI_CONTROLLER
from game_controller import GAME_CONTROLLER
from board_controller import BOARD_CONTROLLER

if __name__ == "__main__":
    # ルート画面の作成
    root = tkinter.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

    # キャンバスウィジェットの配置
    canvas = tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()

    # ボードの描画
    board = BOARD()
    board_ui_controller = BOARD_UI_CONTROLLER(board, canvas)
    board_controller = BOARD_CONTROLLER(board)

    game_controller = GAME_CONTROLLER(board_ui_controller, board_controller, canvas)
    game_controller.update()

    # 実行
    root.mainloop()
