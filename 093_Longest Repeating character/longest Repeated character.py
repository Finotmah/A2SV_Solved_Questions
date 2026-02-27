class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        frq = [0]*26
        l = 0
        max_frq = 0
        result = 0
        for r in range(len(s)):
            index = ord(s[r]) - ord('A')
            frq[index] += 1  #increase frq of new char
            max_frq = max(max_frq, frq[index]) #update the most frequent
            while (r - l + 1)  > k + max_frq: # check window size
                frq[ord(s[l]) - ord('A')] -= 1
                l += 1
            result = max(r - l + 1, result)
        
        return result

            
                
