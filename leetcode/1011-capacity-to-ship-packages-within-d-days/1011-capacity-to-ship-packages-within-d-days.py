class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        def canship(capacity):
            day = 1
            curr = 0

            for weight in weights:
                if curr + weight > capacity:
                    day += 1
                    curr = 0
                curr += weight
            return day <= days

        while left < right:
            mid = (left + right)//2
            if canship(mid):
                right = mid
            else:
                left = mid + 1
        return left