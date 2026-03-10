from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_s = float('-inf')
        left = 0
        i_queue = deque()
        d_queue = deque()
        for r in range(len(nums)):
            while d_queue and nums[r] > nums[d_queue[-1]]:
                d_queue.pop()
            d_queue.append(r)
            while i_queue and nums[r] < nums[i_queue[-1]]:
                i_queue.pop()
            i_queue.append(r)

            while nums[d_queue[0]] -  nums[i_queue[0]] > limit:
                if nums[left] == nums[i_queue[0]]:
                    i_queue.popleft()
                if nums[left] == nums[d_queue[0]]:
                    d_queue.popleft()
                left += 1
            
            max_s = max(max_s, r - left + 1)
        return max_s