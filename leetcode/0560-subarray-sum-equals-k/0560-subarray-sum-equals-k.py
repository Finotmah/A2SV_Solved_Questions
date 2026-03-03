class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_c = {0: 1}
        pre_sum = 0
        res = 0

        for  num in nums:
            pre_sum += num 
             
            if (pre_sum - k) in pre_c:
                res += pre_c[pre_sum - k]
            
            pre_c[pre_sum] = pre_c.get(pre_sum, 0) + 1
        return res