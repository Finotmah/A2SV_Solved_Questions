from collections import Counter
class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if set(word1) != set(word2):
            return False
        count1 = Counter(word1)
        count2 = Counter(word2)

        sorted_count1 = sorted(count1.values())
        sorted_count2 = sorted(count2.values())

        if sorted_count1 != sorted_count2:
            return False
        else:
            return True

        
