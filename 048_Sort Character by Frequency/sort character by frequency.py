from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        
        count = Counter(s)

        sorted_char_tuble = sorted(count.items(), key = lambda x: x[1], reverse = True)
        result = ""
        for char_tuple in sorted_char_tuble:
            result += char_tuple[0] * char_tuple[1]
        
        return result

        
