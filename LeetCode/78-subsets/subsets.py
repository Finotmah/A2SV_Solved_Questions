class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        powerset = [[]]

        for num in nums:
            subsets = []
            for s in powerset:
                subsets.append(s+[num])
            powerset.extend(subsets)

        return powerset