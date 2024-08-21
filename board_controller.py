from board_checker import BOARD_CHECKER


class BOARD_CONTROLLER:
    def __init__(self, board):
        self.board = board
        self.board_checker = BOARD_CHECKER(self.board)

    def can_update_board(self, pos, player):
        can_turn_pieces = self.board_checker.get_turn_pieces(pos, player)
        return len(can_turn_pieces) != 0

    def update_board(self, pos, player):
        can_turn_pieces = self.board_checker.get_turn_pieces(pos, player)
        self.board.set_status(pos, player)
        for piece in can_turn_pieces:
            self.board.turn_status(piece)
