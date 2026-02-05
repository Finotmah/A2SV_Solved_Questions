class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_count = dict()
        num_twice_count = []

        for num in nums:
            if num not in num_count:
                num_count[num] = 0
            num_count[num] += 1
            
            if num_count[num] == 2:
                num_twice_count.append(num)

        return num_twice_count

        
