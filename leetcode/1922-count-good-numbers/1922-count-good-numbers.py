class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        def helper(x,n):
            if n == 0:
                return 1
            half = helper(x,n//2)

            if n % 2 == 0:
                return (half * half)%mod
            else:
                return (half * half * x)%mod
        
        even_pos = (n + 1)//2
        odd_pos = n//2
        return (helper(5,even_pos) *  helper(4,odd_pos))%mod
        