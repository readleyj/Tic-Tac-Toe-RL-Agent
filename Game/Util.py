import numpy as np


def all_equal(seq, elem):
    return seq.count(elem) == len(seq)


def check_for_identical_rows(board, elem):
    top_row = board[0]
    middle_row = board[1]
    bottom_row = board[2]
    left_column = [row[0] for row in board]
    middle_column = [row[1] for row in board]
    right_column = [row[2] for row in board]
    right_diagonal = [board[x][x] for x in range(3)]
    left_diagonal = [board[2 - x][x] for x in range(3)]

    if (all_equal(top_row, elem) or all_equal(middle_row, elem) or
        all_equal(bottom_row, elem) or all_equal(left_column, elem) or
        all_equal(middle_column, elem) or all_equal(right_column, elem) or
            all_equal(right_diagonal, elem) or all_equal(left_diagonal, elem)):
        return True


def coord_to_pos(coord):
    row, col = position
    return row * 3 + col


def pos_to_coord(position):
    return [position // 3, position % 3]


def save_to_json(path, file_name, data):
    file_path_name = path + '/' + file_name + '.npy'
    np.save(file_path_name, data)
