class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def ispossible(distance):
            count = 1
            last_b = position[0]

            for i in range(1, len(position)):
                if position[i] - last_b >= distance:
                    count += 1
                    last_b = position[i]
                if count >= m:
                    return True
            return False
        left, right = 1, position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if ispossible(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result