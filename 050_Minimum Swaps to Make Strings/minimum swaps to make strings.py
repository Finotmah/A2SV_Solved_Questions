class Solution(object):
    def minimumSwap(self, s1, s2):

        min_ops = 0
        xy = 0
        yx = 0

        for i in range(len(s1)):

            if s1[i] == "x" and s2[i] == "y":
                xy += 1

            elif s1[i] == "y" and s2[i] == "x":
                yx += 1

        # impossible case
        if (xy + yx) % 2 != 0:
            return -1

        min_ops = xy // 2
        min_ops += yx // 2
        min_ops += (xy % 2) * 2

        return min_ops
