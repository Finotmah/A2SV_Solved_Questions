class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        rem_frq = dict()
        pre_sum = 0
        count = 0
        rem_frq[0] = 1

        for i in range(len(nums)):
            pre_sum += nums[i]
            remainder = pre_sum % k
            if remainder in rem_frq:
                count += rem_frq.get(remainder, 0)
            rem_frq[remainder] = rem_frq.get(remainder,0) + 1
        return count