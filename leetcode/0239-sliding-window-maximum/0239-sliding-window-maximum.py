from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        l = 0
        for i,num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i - l + 1 == k:
                if queue:
                    res.append(nums[queue[0]])
                if l == queue[0]:
                    queue.popleft()
                
                l += 1
            
        return res
        