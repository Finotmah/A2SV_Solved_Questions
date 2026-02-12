from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote_C = Counter(ransomNote)
        magazine_C = Counter(magazine)

        for letter in ransomNote:
            if ransomNote_C[letter] != 0:
                
                if ransomNote_C[letter] > magazine_C.get(letter, 0):
                    return False

        return True
