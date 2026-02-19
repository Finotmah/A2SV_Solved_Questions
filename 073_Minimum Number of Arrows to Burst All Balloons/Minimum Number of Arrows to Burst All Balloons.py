class Solution(object):
    def findMinArrowShots(self, points):

        if not points:
            return 0
        
        sort_points = sorted(points, key=lambda x: x[1])
        num_arrow = 1
        arrow_pos = sort_points[0][1]  # shoot first arrow at end of first balloon

        for i in range(1, len(sort_points)):
            if sort_points[i][0] > arrow_pos:
                num_arrow += 1
                arrow_pos = sort_points[i][1]

        return num_arrow
