class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        pre = 0
        mymap = {0:-1}
        for i in range(len(nums)):
            pre +=  nums[i]
            if k != 0:
                pre %= k
            if pre in mymap:
                if i - mymap[pre] >= 2:
                    return True
            else:
                mymap[pre] = i

        return False