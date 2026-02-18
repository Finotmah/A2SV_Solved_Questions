class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        rot0 = True
        rot90 = True
        rot180 = True
        rot270 = True
        
        for i in range(n):
            for j in range(n):
                
                # 0°
                if mat[i][j] != target[i][j]:
                    rot0 = False
                
                # 90°
                if mat[i][j] != target[j][n-1-i]:
                    rot90 = False
                
                # 180°
                if mat[i][j] != target[n-1-i][n-1-j]:
                    rot180 = False
                
                # 270°
                if mat[i][j] != target[n-1-j][i]:
                    rot270 = False
        
        return rot0 or rot90 or rot180 or rot270
