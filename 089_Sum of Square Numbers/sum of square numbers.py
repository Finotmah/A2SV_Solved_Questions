class Solution(object):
    def judgeSquareSum(self, c):
        l = 0
        r = int(c**0.5)     
        while l <= r:
            s = l**2 + r**2
            if s == c:
                return True
            elif s < c:
                l += 1
            else:
                r -= 1
        return False
        
        
