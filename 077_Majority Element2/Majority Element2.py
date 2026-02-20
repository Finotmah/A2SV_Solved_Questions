from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        mins = len(nums) // 3
        result = []
        
        for num in counts:
            if counts[num] > mins:
                result.append(num)
        
        return result
