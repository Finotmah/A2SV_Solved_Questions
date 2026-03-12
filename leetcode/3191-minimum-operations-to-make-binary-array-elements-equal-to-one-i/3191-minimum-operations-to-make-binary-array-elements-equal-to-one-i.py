from collections import deque
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        count = 0
        i = 0
        k = 3
        for i in range(len(nums)):
            if nums[i] == 1:
                continue
            else:
                if i + k <= len(nums):
                    for j in range(i,i + k):
                        nums[j] = 0 if nums[j] else 1
                    count += 1
                else:
                    return -1
        return count
                    

        
