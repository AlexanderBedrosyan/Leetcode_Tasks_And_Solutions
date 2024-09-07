class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(row, col, grid):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]):
                return
            if grid[row][col] == '0':
                return

            grid[row][col] = '0'

            dfs(row - 1, col, grid)
            dfs(row + 1, col, grid)
            dfs(row, col - 1, grid)
            dfs(row, col + 1, grid)

        rows = len(grid)
        columns = len(grid[0])
        counter = 0

        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == '1':
                    dfs(row, col, grid)
                    counter += 1

        return counter

solve = Solution()
print(solve.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
print(solve.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))