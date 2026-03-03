class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.pre = [0]*(len(self.nums) + 1)
        self.pre[0] = 0
        for i in range(1,len(self.nums)+1):
            self.pre[i] = self.pre[i-1] + self.nums[i-1]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.pre[right + 1] - self.pre[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)