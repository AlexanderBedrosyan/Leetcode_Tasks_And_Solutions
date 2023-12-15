# An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).
#
# Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
from typing import List


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        needed_line = sorted([ch for ch in range(1, len(matrix) + 1)])
        for line in matrix:
            if not all(map(lambda x: x in line, needed_line)):
                return False

        for col in range(len(matrix)):
            column = [matrix[row][col] for row in range(len(matrix))]
            if not all(map(lambda x: x in column, needed_line)):
                return False
        return True


solve = Solution()
print(solve.checkValid([[1,2,3],[3,1,2],[2,3,1]]))