class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        char_count = dict()
        len_sum_of_good_word = 0
        for char in chars:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        
        word_char_count = dict()
        for word in words:
            
            for char in word:
                if char not in word_char_count:
                    word_char_count[char] = 0
                word_char_count[char] += 1
            is_good = True
            for char in word:
                if char not in char_count or word_char_count[char] > char_count[char]:
                    is_good = False
            if is_good:
                len_sum_of_good_word += len(word)
            word_char_count.clear()
        return len_sum_of_good_word
            


        
