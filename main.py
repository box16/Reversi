import tkinter
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from settings import BOARD_DRAW_OFFSET
from settings import CELL_SIZE
from board import BOARD
from board_drawer import BOARD_DRAWER
from game_controller import GAME_CONTROLLER
from board_checker import BOARD_CHECKER


def convert_board_pos(event):
    if (event.x < BOARD_DRAW_OFFSET) or (event.x > WINDOW_WIDTH - BOARD_DRAW_OFFSET):
        raise Exception("範囲外")
    if (event.y < BOARD_DRAW_OFFSET) or (event.y > WINDOW_HEIGHT - BOARD_DRAW_OFFSET):
        raise Exception("範囲外")

    return (
        int((event.x - BOARD_DRAW_OFFSET) / CELL_SIZE),
        int((event.y - BOARD_DRAW_OFFSET) / CELL_SIZE),
    )


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    canvas = tkinter.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.place(x=0, y=0)
    turn_label = tkinter.Label(root, font=("Arial", 18))
    turn_label.pack(side="top", anchor="n")

    board = BOARD()
    board_drawer = BOARD_DRAWER(canvas)
    board_checker = BOARD_CHECKER()
    game_controller = GAME_CONTROLLER(board, board_drawer, board_checker, turn_label)

    game_controller.prepare()
    canvas.bind(
        "<Button-1>", lambda event: game_controller.proceed(convert_board_pos(event))
    )

    root.mainloop()
