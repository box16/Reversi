from settings import GREEN
from settings import WINDOW_WIDTH, WINDOW_HEIGHT
from settings import BOARD_BEGIN_OFFSET
from settings import CELL_LEN


class BOARD_UI:
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
        # これの責務をどこかに移すか
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
