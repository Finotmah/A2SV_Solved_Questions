class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        c = set()
        diagonal = set()        
        anti_diagonal = set()

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in c or (row - col) in diagonal or (row + col) in anti_diagonal:
                    continue
                # place queen
                board[row][col] = "Q"
                c.add(col)
                diagonal.add(row - col)
                anti_diagonal.add(row + col)
                backtrack(row + 1)
                # remove queen (backtrack)
                board[row][col] = "."
                c.remove(col)
                diagonal.remove(row - col)
                anti_diagonal.remove(row + col)

        backtrack(0)
        return res