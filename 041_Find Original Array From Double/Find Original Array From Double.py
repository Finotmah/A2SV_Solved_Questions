from collections import Counter

class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed) % 2:
            return []

        count = Counter(changed)
        original = []
        changed = sorted(count, key=abs)
        for num in changed:

            if count[num] > count[2*num]:
                return []

            if num == 0:
                original.extend([0] * (count[num] // 2))
            else:
                original.extend([num] * count[num])
                count[2*num] -= count[num]

        return original
