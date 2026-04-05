class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(s,path):
            res.append(path[:])
            for j in range(s,len(nums)):
                if j > s and nums[j] == nums[j-1]:
                    continue
                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()

            
        backtrack(0,[])
        return res