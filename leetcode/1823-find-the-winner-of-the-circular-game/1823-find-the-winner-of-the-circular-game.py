from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        w = 1

        for i in range(2,n+1):
            w = (w + k-1)%i+1
        return w