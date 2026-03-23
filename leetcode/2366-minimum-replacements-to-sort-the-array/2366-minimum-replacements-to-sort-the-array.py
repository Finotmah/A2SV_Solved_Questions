class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ops = 0
        pre = nums[-1]

        for i in range(len(nums)-2, -1,-1):
            if nums[i] <= pre:
                pre = nums[i]
            else:
               num_s = (nums[i] + pre -1) // pre
               ops += num_s - 1
               pre =  nums[i]//num_s
        return ops