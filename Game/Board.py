import Util as util


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.state = '123456789'

    def is_position_empty(self, position):
        row, col = position
        return (self._board_state[row - 1][col - 1] == '-')

    def set_position_value(self, position, letter):
        row, col = position
        self._board[row - 1][col - 1] = player_letter
        self._state = util.change_board_state(self._state, row, col, letter)

    def make_move(self, position, player_letter):
        if (self.is_position_empty(position)):
            self.set_position_value(position, player_letter)
        else:
            raise Exception('Position already occupied')

    def game_over(self):
        return check_for_identical_rows(self.board)
