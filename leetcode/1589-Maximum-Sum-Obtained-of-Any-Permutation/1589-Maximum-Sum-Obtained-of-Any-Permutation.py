class Solution(object):
    def maxSumRangeQuery(self, nums, requests):
        """
        :type nums: List[int]
        :type requests: List[List[int]]
        :rtype: int
        """
        n =  len(nums)
        pre_s = [0] * (n + 1)

        mod = 10**9 + 7
        for l, r in requests:
            pre_s[l] += 1
            pre_s[r+1] -= 1
        
        for i in range(1, n+1):
            pre_s[i] += pre_s[i-1]
        pre_s = pre_s[:-1]
        
        # to put big num in index with high frequency
        pre_s.sort()
        nums.sort()
        sums = 0
        for i in range(n):
            sums += pre_s[i] * nums[i]
        
        return sums % mod