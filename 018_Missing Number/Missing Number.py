class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        total_sum = n * (n + 1) // 2
        return total_sum - sum(nums)
        
