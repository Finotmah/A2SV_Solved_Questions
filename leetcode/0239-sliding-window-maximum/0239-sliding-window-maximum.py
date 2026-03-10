from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        res = []
        for i,num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if i + 1 == k:
                if queue:
                    res.append(nums[queue[0]])
            if i + 1 > k:
                if i - k == queue[0]:
                    queue.popleft()
                res.append(nums[queue[0]])
            
        return res
        