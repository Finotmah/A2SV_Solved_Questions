class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [ [False for i in range(len(grid[0]))] for j in range(len(grid))]

        def isbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(grid,visited, r,c):
            
            if not isbound(r,c):
                return 1
            if grid[r][c] == 0:
                return 1
            if visited[r][c]:
                return 0

            visited[r][c] = True
            perimeter = 0

            for row_change, col_change in directions:
                new_row = r + row_change
                new_col = c + col_change
                
                perimeter += dfs(grid, visited, new_row,new_col)
            return perimeter

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(grid,visited,i,j)
        return 0
        
        