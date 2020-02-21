
def start_game():
    """Start the game."""
    size_of_field = input('Input size of field between 3 and 5.\n')

    while size_of_field not in ['3', '4', '5']:
        size_of_field = input('Wrong. Input size of field between 3 and 5.\n')

    size_of_field = int(size_of_field)
    game = Game(size_of_field)
    game.play()
    return


class Game:
    def __init__(self, size: int):
        """
        Initialization size, separators and values
        :param size: size of field
        """
        self.size = size
        self.vertical_separator = '|'
        self.horizontal_separator = ' ' + '-' * (4 * self.size - 1)
        self.values = [['   ' for _ in range(self.size)] for _ in range(self.size)]
        self.player = 'x'

    def _print(self):
        """
        Print the field
        """
        print(' ' + ' '.join([' {i} '.format(i=i + 1) for i in range(self.size)]))
        for i in range(2 * self.size - 1):
            if i % 2:
                print(self.horizontal_separator)
            else:
                print('a b c d e'[i], end='')
                for j in range(2 * self.size - 1):
                    if j % 2:
                        print(self.vertical_separator, end='')
                    else:
                        print(self.values[i // 2][j // 2], end='')
                print('')

    def _check_cell(self, row_number: int, column_number: int) -> str:
        """
        Check if you may write to cell
        :return: Success or Fail
        """
        if row_number in range(self.size) and column_number in range(self.size) \
                and self.values[row_number][column_number] == '   ':
            return 'Success'
        else:
            return 'Fail'

    def _update_value(self, row_number: int, column_number: int):
        """
        Set x or o to the cell
        """
        self.values[row_number][column_number] = f' {self.player} '

    def _check_horizontal_lines(self) -> str:
        """
        Check if one of horizontal lines contains of only x or only o
        :return: First player won. or Second player won. or empty string
        """
        for i in range(self.size):
            if self.values[i] == [' x '] * self.size:
                return 'First player won.'
            elif self.values[i] == [' o '] * self.size:
                return 'Second player won.'
        return ''

    def _check_vertical_lines(self) -> str:
        """
        Check if one of vertical lines contains of only x or only o
        :return: First player won. or Second player won. or empty string
        """
        for i in range(self.size):
            column = ''
            for j in range(self.size):
                column += self.values[j][i]
                if column == ' x ' * self.size:
                    return 'First player won.'
                elif column == ' o ' * self.size:
                    return 'Second player won.'
        return ''

    def _check_diagonal_lines(self) -> str:
        """
        Check if one of diagonal lines contains of only x or only o
        :return: First player won. or Second player won. or empty string
        """
        diagonal = ''
        for i in range(self.size):
            diagonal += self.values[i][i]
        if diagonal == ' x ' * self.size:
            return 'First player won.'
        elif diagonal == ' x=o ' * self.size:
            return 'Second player won.'
        diagonal = ''
        for i in range(self.size):
            diagonal += self.values[i][-i-1]
        if diagonal == ' x ' * self.size:
            return 'First player won.'
        elif diagonal == ' o ' * self.size:
            return 'Second player won.'
        return ''

    def _change_player(self):
        """
        Switch x to o or o to x
        """
        if self.player == 'x':
            self.player = 'o'
        else:
            self.player = 'x'

    def play(self):
        """
        Main function, allow to play. Ask you to input filed size and coordinates for each step
        :return: Which player won or draw
        """
        self._print()
        rounds = 0
        while rounds < self.size ** 2:
            coordinates = input('\nInput coordinates\n')
            if len(coordinates) == 2 and coordinates[1] in '12345':
                row_index, column_number = coordinates[0], int(coordinates[1]) - 1
                row_number = 'abcde'.find(row_index)
                if self._check_cell(row_number, column_number) == 'Fail':
                    print('You inputted the shit. Try again.')
                else:
                    rounds += 1
                    self._update_value(row_number, column_number)
                    self._change_player()
                    self._print()
                    if self._check_vertical_lines() != '':
                        print(self._check_vertical_lines())
                        return
                    elif self._check_horizontal_lines() != '':
                        print(self._check_horizontal_lines())
                        return
                    elif self._check_diagonal_lines() != '':
                        print(self._check_diagonal_lines())
                        return
            else:
                print('You inputted the shit. Try again.')
        print('Nobody won. Draw. The End')
        return


if __name__ == "__main__":
    start_game()
