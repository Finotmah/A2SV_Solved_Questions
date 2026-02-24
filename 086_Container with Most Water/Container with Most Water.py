class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height)-1
        max_area = 0

        while l < r:
            c_width = r - l
            c_height = min(height[l],height[r])
            c_area = c_width *c_height
            max_area = max(max_area,c_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_area


        
