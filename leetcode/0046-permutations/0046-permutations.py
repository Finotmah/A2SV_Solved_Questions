class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        isUsed = [0]*len(nums)
        def backtracking():
            if len(nums) ==len(path):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if isUsed[i]:
                    continue
                path.append(nums[i])
                isUsed[i] = 1
                backtracking()
                path.pop()
                isUsed[i] = 0
        backtracking()
        return res

            