class Solution(object):
    def transpose(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        new_matrix = [[0]*rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                new_matrix[c][r] = matrix[r][c]
        return new_matrix
            
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
