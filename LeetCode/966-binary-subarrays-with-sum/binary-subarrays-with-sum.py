class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n = len(nums)
        sums = 0
        num_sub = 0
        frq = dict()
        for num in nums:
            sums += num
            if sums == goal:
                num_sub += 1
            
            if sums - goal in frq:
                num_sub += frq[sums - goal]
            
            frq[sums] = frq.get(sums,0) + 1
        
        return num_sub

        
        