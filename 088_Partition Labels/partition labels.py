class Solution(object):
    def partitionLabels(self, s):
        last_index = dict()
        for i in range(len(s)):
            last_index[s[i]] = i
        
        partitions = []
        start = 0
        end = 0
        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                partitions.append(end - start + 1)
                start = i + 1
        return partitions
        """
        :type s: str
        :rtype: List[int]
        """
        
