class Solution(object):
    def smallestEvenMultiple(self, n):
        if n % 2 != 0:
            return 2*n
        numTwo = 0
        while n % 2 == 0:
            n /= 2
            numTwo += 1
        return 2**numTwo*n
        """
        :type n: int
        :rtype: int
        """
        
