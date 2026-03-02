class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        
        letters = [ord(c) - ord('a') for c in s]
        diff = [0] * (n + 1)
        
        for l, r, direction in shifts:
            if direction == 1:
                diff[l] += 1
                diff[r+1] -= 1
            else:
                diff[l] -= 1
                diff[r+1] += 1
        
        for i in range(1, n):
            diff[i] += diff[i-1]
        
        result = []
        for i in range(n):
            letters[i] = (letters[i] + diff[i]) % 26
            result.append(chr(ord('a') + letters[i]))
        return ''.join(result)