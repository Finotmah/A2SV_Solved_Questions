class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        s1 = len(needle)
        s2 = len(haystack)
        l = 0
        r = len(needle)
        w = haystack[:s1]
        if needle in haystack:
            if w == needle:
                return 0
            else:
                for i in range(s1,s2):
                    l += 1
                    r += 1
                    w = haystack[l:r]
                    if w == needle:
                        return l
        else:
            return -1           

