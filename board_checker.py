class BOARD_CHECKER:
    def _get_can_turn_pieces(self, board, base_pos, vector):
        range_ = 0
        result = []
        while True:
            check_pos = (
                base_pos[0] + (vector[0] * range_),
                base_pos[1] + (vector[1] * range_),
            )
            if not board.is_valid_pos(check_pos):
                return []
            if board.is_empty(check_pos):
                return []
            if board.get(check_pos) == board.get(base_pos):
                result.append(check_pos)
                range_ += 1
                continue
            return result

    def get_can_place_pos(self, board, player):
        board_len = board.get_side_len()
        pos_list = [(i, j) for i in range(board_len) for j in range(board_len)]
        visinity = [(i, j) for i in (-1, 0, 1) for j in (-1, 0, 1)]
        visinity.remove((0, 0))

        result = {}
        for p in pos_list:
            if not board.is_empty(p):
                continue

            can_turn_pieces = []
            for v in visinity:
                check_pos = (p[0] + v[0], p[1] + v[1])
                if not board.is_valid_pos(check_pos):
                    continue
                if board.is_empty(check_pos):
                    continue
                if board.get(check_pos) == player:
                    continue
                tmp = self._get_can_turn_pieces(board, check_pos, v)
                if not tmp:
                    continue
                can_turn_pieces += tmp

            if not can_turn_pieces:
                continue
            result[p] = can_turn_pieces
        return result
