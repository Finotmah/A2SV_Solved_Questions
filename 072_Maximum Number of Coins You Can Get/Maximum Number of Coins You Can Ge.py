class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()

        start_index = len(piles)//3
        max_coin = 0
        second_larg_num_index = -2
        
        for i in range(start_index,0, -1):
            max_coin += piles[second_larg_num_index]
            second_larg_num_index -= 2

        return max_coin


