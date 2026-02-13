class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        rows = len(mat)
        cols = len(mat[0])

        i = 0
        j = 0

        dirn = 1
        result = []
        for _ in range(rows*cols):
            
            result.append(mat[i][j])

            #upward
            if dirn == 1:
                if j == cols -1:
                    i += 1
                    dirn = -1
                elif i == 0:
                    j += 1
                    dirn = -1
                else:
                    i -= 1
                    j += 1
                    
            #downward
            else:
                if i == rows -1:
                    j += 1
                    dirn = 1
                elif j == 0:
                    i += 1
                    dirn = 1
                else:
                    i += 1
                    j -= 1
                    
        return result
