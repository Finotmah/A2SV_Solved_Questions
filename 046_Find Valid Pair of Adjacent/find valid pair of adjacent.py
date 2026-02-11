from collections import Counter
class Solution(object):
    def findValidPair(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)

        for i in range(len(s)):
            if i + 1 < len(s):
                if s[i] != s[i + 1] and count[s[i]] == int(s[i]):
                    if count[s[i + 1]] == int(s[i + 1]):
                        return s[i] + s[i + 1]
       
        return ""
                    
