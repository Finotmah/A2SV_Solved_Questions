class Solution(object):
    def wordPattern(self, pattern, s):

        siz1 = len(pattern)
        words = s.split()
        siz2 = len(words)

        if siz1 != siz2:
            return False

        mapping = {}   # char -> word
        seen = set()   # words already mapped

        for i in range(siz1):

            char = pattern[i]
            word = words[i]

            if char in mapping:
                # char already mapped → must match
                if mapping[char] != word:
                    return False
            else:
                # word already used by another char
                if word in seen:
                    return False

                mapping[char] = word
                seen.add(word)

        return True
