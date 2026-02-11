from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        
        s_count = Counter(s)
        t_count = Counter(t)
        min_ops = 0
        seen = set()
        
        for char in s:
            if char in seen:
                continue
                
            ops = s_count[char] - t_count[char]
            if ops > 0:
                min_ops += ops

            seen.add(char)
        return min_ops

            
            



        

            
        
