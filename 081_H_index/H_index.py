class Solution(object):
    def hIndex(self, citations):

        citations.sort()
        n = len(citations)

        h_indexs = []

        for i in range(n + 1):   # only up to n
            num_p = 0
            for j in range(n):
                if citations[j] >= i:
                    num_p += 1

            if num_p >= i:
                h_indexs.append(i)

        if not h_indexs:
            return 0

        return max(h_indexs)
