class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        min_move = 0
        while target > 1 and maxDoubles > 0:
            if target % 2 == 0:
                target = target//2
                maxDoubles -= 1
            else:
                target -= 1
            min_move += 1

        min_move = min_move + target - 1
        return min_move