class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # i +
        # j +
        m = len(grid) # num of rows
        n = len(grid[0]) # num of cols
        for i in range(1, n):
            grid[0][i] += grid[0][i-1] # total of first row
        for i in range(1, m):           
            grid[i][0] += grid[i-1][0] # total of first col
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) # find the min of top or left 
        return grid[-1][-1]