class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        st_num = str(n)
        is_happy = False
        seen = set()
        if n == 1:
            return True
        while n != 1:
            if n in seen:
                return False
            sums = 0
            seen.add(n)
            while n > 0:
                digit = n % 10
                sums += digit**2
                n = n // 10
            n = sums
            if n == 1:
                return True
            
        

            
            
        
