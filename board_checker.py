class BOARD_CHECKER:
    VICINITY = [-1, 0, 1]

    def __init__(self):
        pass

    def _is_piece_exist(self, board, check_pos):
        if not board.is_valid_pos(check_pos):
            return False
        if board.is_empty(check_pos):
            return False
        return True

    def _get_exploration_candidates(self, board, pos):
        exploration_candidates = []
        for i in self.VICINITY:
            for j in self.VICINITY:
                if (i, j) == (0, 0):
                    continue

                check_pos = (pos[0] + i, pos[1] + j)
                if not self._is_piece_exist(board, check_pos):
                    continue
                if board.is_empty(check_pos):
                    continue
                if board.get_status(check_pos) == board.get_status(pos):
                    continue
                exploration_candidates.append((i, j))
        return exploration_candidates

    def get_turn_pieces(self, board, pos, now_color):

        if not board.is_valid_pos(pos):
            raise Exception("範囲外")

        exploration_candidates = self._get_exploration_candidates(board, pos)
        if not exploration_candidates:
            return []

        turn_pieces = []
        for ec in exploration_candidates:
            turn_piece_temp = []
            range = 1
            while True:
                check_pos = (pos[0] + (ec[0] * range), pos[1] + (ec[1] * range))
                if not board.is_valid_pos(check_pos):
                    break
                elif board.is_empty(check_pos):
                    break
                elif now_color == board.get_status(check_pos):
                    turn_pieces += turn_piece_temp
                    break
                else:
                    turn_piece_temp.append(check_pos)
                    range += 1
                    continue
        return turn_pieces
