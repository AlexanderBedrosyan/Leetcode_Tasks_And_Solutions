# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following
# rules:
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def square_checker(square):
            all_charts = []
            for line in square:
                for ch in line:
                    if ch not in all_charts or ch == '.':
                        all_charts.append(ch)
                    else:
                        return False
            return True


        n = 9

        for i in range(0, n):
            row = []
            col = []
            for j in range(0, n):
                if board[i][j] not in row or board[i][j] == '.':
                    row.append(board[i][j])
                else:
                    return False
                if board[j][i] not in col or board[j][i] == '.':
                    col.append(board[j][i])
                else:
                    return False


        for row_start in range(0, len(board), 3):
            for col_start in range(0, len(board), 3):
                square = [board[i][col_start:col_start + 3] for i in range(row_start, row_start + 3)]

                if not square_checker(square):
                    return False

        return True


solve = Solution()
print(solve.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

print(solve.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))