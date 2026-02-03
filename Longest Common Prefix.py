class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""
        
        common = ""
        for i,char in enumerate(strs[0]):
            print(i,char)
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != char:
                    return common
            common += char
        return common


        '''if not strs:
            return ""
        prefix = strs[0]
        
        for word in strs[1:]:
            while word[:len(prefix)] != prefix:
               
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
'''


