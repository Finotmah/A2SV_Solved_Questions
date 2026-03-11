from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_a = 0
        heights.append(0)
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                max_h = heights[stack.pop()]
                if not stack:
                    width = i
                else:
                    width = i - stack[-1] - 1
                max_a = max(max_a, max_h * width)
            stack.append(i)
            
        return max_a