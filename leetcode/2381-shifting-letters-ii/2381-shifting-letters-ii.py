class Solution(object):
    def shiftingLetters(self, s, shifts):
        """
        :type s: str
        :type shifts: List[List[int]]
        :rtype: str
        """
        n = len(s)
        letters = []

        for c in s:
            letters.append(ord(c)-ord('a'))

        prefix_sum = [0] * (n + 1)

        for l, r, d in shifts:
            if d == 1:
                prefix_sum[l] += 1
                prefix_sum[r+1] -= 1
            else:
                prefix_sum[l] -= 1
                prefix_sum[r+1] += 1
        
        result = []

        for i in range(1,n + 1):
            prefix_sum[i] += prefix_sum[i-1]
        
        for i in range(n):
            letters[i] = (letters[i] + prefix_sum[i])%26
            result.append(chr(ord('a')+ letters[i]))
        
        return ''.join(result)