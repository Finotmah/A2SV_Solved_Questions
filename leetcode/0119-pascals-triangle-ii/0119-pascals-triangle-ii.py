class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tra = [[1]]

        for i in range(1,rowIndex + 1):
            pre = tra[-1]
            n_row = [1]
            for j in range(1,i):
                n_row.append(pre[j-1] + pre[j])
            n_row.append(1)
            tra.append(n_row)
        return tra[rowIndex]