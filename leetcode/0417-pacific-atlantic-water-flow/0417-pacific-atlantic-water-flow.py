class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        pac, atl = set(), set()
        def isbound(r,c):
            return r < 0 or c < 0 or r >= rows or c >= cols
        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (nr, nc) in visited:
                    continue
                if isbound(nr,nc):
                    continue
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, visited)

        
        for c in range(cols):
            dfs(0, c, pac)
        for r in range(rows):
            dfs(r, 0, pac)

        for c in range(cols):
            dfs(rows - 1, c, atl)
        for r in range(rows):
            dfs(r, cols - 1, atl)

        return list(pac & atl)