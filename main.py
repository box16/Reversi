import tkinter
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from settings import BOARD_DRAW_OFFSET
from settings import CELL_SIZE
from board import BOARD
from board_drawer import BOARD_DRAWER
from game_controller import GAME_CONTROLLER
from board_controller import BOARD_CONTROLLER


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
    canvas.pack()

    board = BOARD()
    board_drawer = BOARD_DRAWER(canvas)
    board_controller = BOARD_CONTROLLER(board)
    game_controller = GAME_CONTROLLER(board, board_drawer, board_controller)

    board_drawer.draw(board)
    canvas.bind(
        "<Button-1>", lambda event: game_controller.proceed(convert_board_pos(event))
    )

    root.mainloop()
