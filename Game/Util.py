

def all_elems_equal(seq):
    return seq.count(seq[0]) == len(seq)


def check_for_identical_rows(board):
    top_row = board[0]
    middle_row = board[1]
    bottom_row = board[2]
    left_column = board[:, 0]
    middle_column = board[:, 1]
    right_column = board[:, 2]
    right_diagonal = [board[x][x] for x in range(3)]
    left_diagonal = [board[2 - x][x] for x in range(3)]

    if (all_elems_equal(top_row) or all_elems_equal(middle_row) or /
        all_elems_equal(bottom_row) or all_elems_equal(left_column) or /
        all_elems_equal(middle_column) or all_elems_equal(right_column) or /
            all_elems_equal(right_diagonal) or all_elems_equal(left_diagonal)):
        return True


def coord_to_pos(coord):
    row, col = position
    return row * 3 + col


def pos_to_coord(position):
    return [position // 3, position % 3]
