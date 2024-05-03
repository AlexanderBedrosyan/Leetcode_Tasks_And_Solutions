# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        shadow_matrix = []

        for line in matrix:
            new_line = []
            for ch in line:
                new_line.append(ch)
            shadow_matrix.append(new_line)

        n = len(shadow_matrix)

        for i in range(n):
            for j in range(n):
                element_needed = shadow_matrix[i][j]
                row = j
                col = -i - 1

                matrix[row][col] = element_needed

        return matrix



solve = Solution()
print(solve.rotate([
    [1,2,3],
    [4,5,6],
    [7,8,9]]
))

print(solve.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))