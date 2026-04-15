import bisect
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        result = 0
        for house in houses:
            pos = bisect.bisect_left(heaters, house)
            left_distance = 0
            right_distance = 0
            if pos == 0:
                left_distance = float("inf")
            else:
                left_distance = house - heaters[pos-1]
            
            if pos == len(heaters):
                right_distance = float("inf")
            else:
                right_distance = heaters[pos] - house

            result = max(result,min(left_distance,right_distance))
        return result
            
            