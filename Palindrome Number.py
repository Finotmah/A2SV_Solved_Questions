class Solution(object):
    def isPalindrome(self, x):
        num = str(x)
        return num == num[::-1]
        """
        :type x: int
        :rtype: bool
        """
        
