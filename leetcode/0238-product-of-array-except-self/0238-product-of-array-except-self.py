class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n

        l_p = 1
        for i in range(n):
            res[i] = l_p
            l_p *= nums[i]

        r_p = 1
        for i in range(n - 1, -1, -1):
            res[i] *= r_p
            r_p *= nums[i]
        
        return res