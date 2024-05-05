# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        result_holder = [matrix[0][0]]
        position = [0, 0]
        matrix[0][0] = 'V'

        while True:
            if all(all(element == 'V' for element in row) for row in matrix):
                return result_holder

            next_step = directions.pop(0)
            row = position[0] + next_step[0]
            col = position[1] + next_step[1]

            if row < 0 or col < 0 or row == len(matrix) or col == len(matrix[0]):
                directions.append(next_step)
                continue

            if matrix[row][col] == 'V':
                directions.append(next_step)
                continue

            result_holder.append(matrix[row][col])
            matrix[row][col] = 'V'
            position = [row, col]
            directions.insert(0, next_step)


solve = Solution()
print(solve.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solve.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))