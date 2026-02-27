class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        leng = 0
        max_l = 0
        k = 1
        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            while nums[r] != 1 and k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            
            leng = r-l + 1
            max_l = max(max_l, leng)
        
        return max_l -1
