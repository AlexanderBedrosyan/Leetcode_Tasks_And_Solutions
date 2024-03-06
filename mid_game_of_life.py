# According to Wikipedia('s article: "The Game of Life, also known simply as Life, is a cellular automaton devised by '
#                        'the '
#                        'British mathematician John Horton Conway in 1970.")
#
# The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead
# (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following
# four rules (taken from the above Wikipedia article):
#
# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# The next state is created by applying the above rules simultaneously to every cell in the current state, where births
# and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.


class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        new_board = []
        directions = {
            "left": [0, -1],
            "right": [0, 1],
            "down": [1, 0],
            "up": [-1, 0],
            "left_diagonal_up": [-1, -1],
            "left_diagonal_down": [1, -1],
            "right_diagonal_down": [1, 1],
            "right_diagonal_up": [-1, 1],

        }
        rows = len(board)
        columns = len(board[0])

        def validator(row, col):
            if row < 0 or col < 0 or row == rows or col == columns:
                return False
            return True

        def dead_checker(row, col):
            counter = 0
            for position in directions.values():
                new_row = row + position[0]
                new_col = col + position[1]
                if not validator(new_row, new_col):
                    continue
                if new_board[new_row][new_col] == 1:
                    counter += 1

            if counter == 3:
                board[row][col] = 1
            else:
                board[row][col] = 0

        def life_checker(row, col):
            counter = 0
            for position in directions.values():
                new_row = row + position[0]
                new_col = col + position[1]
                if not validator(new_row, new_col):
                    continue
                if new_board[new_row][new_col] == 1:
                    counter += 1

            if counter < 2 or counter > 3:
                board[row][col] = 0
            elif 2 <= counter <= 3:
                board[row][col] = 1

        for line in range(rows):
            new_board.append([board[line][col] for col in range(columns)])


        for row in range(rows):
            for col in range(columns):
                if new_board[row][col] == 0:
                    dead_checker(row, col)
                elif new_board[row][col] == 1:
                    life_checker(row, col)

        return board


solve = Solution()
print(solve.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))