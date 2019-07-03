import Util as util


class Board:
    def __init__(self):
        self.board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        self.state = '123456789'
        self.available_moves = [[x, y] for x in range(3) for y in range(3)]

    def is_position_empty(self, position):
        return position in self.available_moves

    def set_position_value(self, position, letter):
        self.available_moves[self.available_moves.index(position)] = []
        self.state = util.change_board_state(self.state, position, letter)
        row, col = position
        self.board[row - 1][col - 1] = player_letter

    def change_board_state(current_state, position, letter):
        state_number = self.available_moves.index(position)
        new_state = current_state[:state_number] + \
            letter + current_state[state_number + 1:]
        self.state = new_state

    def make_move(self, position, player_letter):
        if (self.is_position_empty(position)):
            self.set_position_value(position, player_letter)
        else:
            raise Exception('Position already occupied')

    def game_over(self):
        return check_for_identical_rows(self.board)
