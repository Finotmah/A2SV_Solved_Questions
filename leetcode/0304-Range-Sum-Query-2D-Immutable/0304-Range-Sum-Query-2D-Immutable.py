class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.row = len(matrix)
        self.col = len(matrix[0])
        print(matrix)
        self.prefixsum = [[0] * (self.col + 1) for _ in range(self.row + 1)]
        for row in range(1, self.row+1):
            for col in range(1, self.col+1):
                self.prefixsum[row][col] = self.matrix[row-1][col -1] + self.prefixsum[row-1][col] + self.prefixsum[row][col -1] - self.prefixsum[row-1][col - 1]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        sums = self.prefixsum[row2 + 1][col2 +1] - self.prefixsum[row2 + 1][col1] - self.prefixsum[row1][col2 + 1] + self.prefixsum[row1][col1]
        return sums


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)