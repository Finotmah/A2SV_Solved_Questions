class Solution:
    def twoSum(self,num,target):
        different ={}
        for i,num in enumerate(num):
            diff = target - num
            if diff in different:
                return [different[diff],i]
            different[num]=i
