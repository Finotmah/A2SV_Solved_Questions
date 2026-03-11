class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        third = float('-inf')
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] < third:
                return True
            while stack and nums[stack[-1]] < nums[i]:
                third = nums[stack.pop()]
            stack.append(i)
        
        return False
