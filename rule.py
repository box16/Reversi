class RULE:
    def __init__(self) -> None:
        pass

    def check(self, board, pos):
        raise NotImplementedError("継承先未定義")


# 名前変更。リファクタ
class PIECE_ARE_NEARBY(RULE):
    def check(self, board, pos, now_color):

        if not board.is_valid_pos(pos):
            raise Exception("範囲外")

        vicinity = [-1, 0, 1]
        can_turn_piece = []
        for i in vicinity:
            for j in vicinity:
                if (i, j) == (0, 0):
                    continue
                check_pos = (pos[0] + i, pos[1] + j)
                is_piece_nearby = board.is_valid_pos(check_pos) and (
                    not board.is_empty(check_pos)
                )
                if not is_piece_nearby:
                    continue

                is_enemy_piece = board.get_status(check_pos) != board.get_status(pos)
                if not is_enemy_piece:
                    continue

                turn_piece_temp = []
                vector = 1
                while True:
                    check_pos = (pos[0] + (i * vector), pos[1] + (j * vector))
                    if not board.is_valid_pos(check_pos):
                        break
                    elif board.is_empty(check_pos):
                        break
                    elif now_color == board.get_status(check_pos):
                        can_turn_piece += turn_piece_temp
                        break
                    else:
                        turn_piece_temp.append(check_pos)
                        vector += 1
                        continue

        return can_turn_piece
