from settings import EMPTY
from settings import BOARD_DRAW_OFFSET
from settings import CELL_SIZE


class BOARD_DRAWER:
    def __init__(self, canvas):
        self.canvas = canvas

    def draw(self, board):
        board_side_len = board.get_side_len()

        for i in range(board_side_len):
            for j in range(board_side_len):
                begin = (
                    BOARD_DRAW_OFFSET + i * CELL_SIZE,
                    BOARD_DRAW_OFFSET + j * CELL_SIZE,
                )

                self.canvas.create_rectangle(
                    begin[0],
                    begin[1],
                    begin[0] + CELL_SIZE,
                    begin[1] + CELL_SIZE,
                    fill=EMPTY,
                    width=2,
                )

                if board.get((i, j)) == EMPTY:
                    continue
                else:
                    r = CELL_SIZE / 10
                    self.canvas.create_oval(
                        begin[0] + r,
                        begin[1] + r,
                        begin[0] + CELL_SIZE - r,
                        begin[1] + CELL_SIZE - r,
                        fill=board.get((i, j)),
                        width=2,
                    )
