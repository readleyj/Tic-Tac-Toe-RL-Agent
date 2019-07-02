from enum import Enum


class BoardIndexes(Enum):
    '01' = 0
    '02' = 1
    '03' = 2
    '10' = 3
    '11' = 4
    '12' = 5
    '20' = 6
    '21' = 7
    '22' = 8


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


def change_board_state(current_state, row, col, letter):
    index_string = str(row) + str(col)
    state_number = BoardIndexes.index_string
    new_state = current_state[:state_number] + \
        letter + current_state[state_number + 1:]
    return new_state
