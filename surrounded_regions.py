class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(row, col, board, symbol):
            if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
                return
            if board[row][col] != 'O':
                return

            board[row][col] = symbol

            dfs(row - 1, col, board, symbol)
            dfs(row + 1, col, board, symbol)
            dfs(row, col + 1, board, symbol)
            dfs(row, col - 1, board, symbol)

        rows = len(board)
        columns = len(board[0])


        for row in range(0, 1): # Up boarder
            for col in range(columns):
                if board[row][col] == 'O':
                    dfs(row, col, board, 'B')

        for row in range(rows - 1, rows): # Down boarder
            for col in range(columns):
                if board[row][col] == 'O':
                    dfs(row, col, board, 'B')

        for row in range(rows): # left boarder
            for col in range(0, 1):
                if board[row][col] == 'O':
                    dfs(row, col, board, 'B')

        for row in range(rows):
            for col in range(columns - 1, columns):
                if board[row][col] == 'O':
                    dfs(row, col, board, 'B')


        for row in range(rows):
            for col in range(columns):
                if board[row][col] == 'O':
                    dfs(row, col, board, 'X')


        for row in range(rows):
            if 'B' in board[row]:
                for col in range(columns):
                    if board[row][col] == 'B':
                        board[row][col] = 'O'

        return board

solve = Solution()
print(solve.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
print(solve.solve([["O","O"],["O","O"]]))
print(solve.solve([["X"]]))
print(solve.solve([["O","X","O"],["X","O","X"],["O","X","O"]]))