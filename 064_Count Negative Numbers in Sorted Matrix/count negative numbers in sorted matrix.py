class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for  i in range(rows):
            for j in range(cols):
                if grid[i][j] < 0:
                    count += 1
        
        return count
        
