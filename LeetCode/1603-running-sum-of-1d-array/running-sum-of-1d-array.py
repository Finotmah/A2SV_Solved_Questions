class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = []
        sums = 0
        for i in range(len(nums)):
            sums += nums[i]
            pre.append(sums)
        return pre