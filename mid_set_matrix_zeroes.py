# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])
        all_zeroes = []

        for row in range(rows):
            for col in range(columns):
                if matrix[row][col] == 0:
                    position = [row, col]
                    all_zeroes.append(position)

        for position in all_zeroes:
            direction = [[0, -1], [0, 1], [1, 0], [-1, 0]]
            current_row = position[0]
            current_col = position[1]
            while direction:
                next_step = direction.pop()
                row = current_row + next_step[0]
                col = current_col + next_step[1]

                if row < 0 or col < 0 or row == rows or col == columns:
                    current_row = position[0]
                    current_col = position[1]
                    continue

                matrix[row][col] = 0

                current_row = row
                current_col = col
                direction.append(next_step)

        return matrix

solve = Solution()
print(solve.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(solve.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
