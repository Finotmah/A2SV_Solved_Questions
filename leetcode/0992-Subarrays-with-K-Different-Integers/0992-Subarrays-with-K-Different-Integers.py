class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmost(k):
            total = 0
            d = {}
            n = 0
            l = 0
            for r in range(len(nums)):
                if nums[r] not in d or d[nums[r]] == 0:
                    n += 1
                d[nums[r]] = d.get(nums[r], 0) + 1
                while n > k:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        n -= 1
                    l += 1

                total += r - l + 1
            return total

        return atmost(k) - atmost(k-1)