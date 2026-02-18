class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        total = rows * cols
        
        r, c = rStart, cStart
        result.append([r, c])
        
        step = 1
        
        while len(result) < total:
            
            # move right
            for _ in range(step):
                c += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            # move down
            for _ in range(step):
                r += 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            step += 1
            
            # move left
            for _ in range(step):
                c -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            # move up
            for _ in range(step):
                r -= 1
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])
            
            step += 1
        
        return result
