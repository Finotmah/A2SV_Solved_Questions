class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        l, r = 0, len(skill) - 1
        
        target_sum = skill[l] + skill[r]
        chemistry = 0
        
        while l < r:
            if skill[l] + skill[r] != target_sum:
                return -1
            chemistry += skill[l] * skill[r]
            l += 1
            r -= 1
        
        return chemistry
        """
        :type skill: List[int]
        :rtype: int
        """
        
