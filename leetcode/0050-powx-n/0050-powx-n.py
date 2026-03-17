class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            res = self.myPow(x,n//2)
            if n % 2:
                return res * res * x
            else:
                return   res * res
        res = helper(x,abs(n))
        if n >= 0:
            return res
        else:
            return 1/res