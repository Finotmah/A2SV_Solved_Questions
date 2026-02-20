from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        counts = Counter(nums)
        min = len(nums) // 3
        result = []
        
        for num in counts:
            if counts[num] > min:
                result.append(num)
        
        return result
