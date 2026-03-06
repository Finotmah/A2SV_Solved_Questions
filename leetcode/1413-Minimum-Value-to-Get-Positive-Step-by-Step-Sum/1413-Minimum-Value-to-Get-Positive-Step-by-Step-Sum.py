class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre_sum = [0]*(len(nums)+1)
        pre_sum[0] = 0
        min_pre = float('inf')
        for i in range(1,len(nums)+1):
            pre_sum[i] = pre_sum[i-1] + nums[i-1]
            min_pre = min(min_pre,pre_sum[i])
        
        min_start = 1 - min_pre
        while min_start + min_pre < 1 or min_start <= 0:
            min_start += 1
        return min_start