class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(s,path):
            if len(path) >= 2:
                res.append(path[:])
            seen = set()
            for j in range(s,len(nums)):
                if path and nums[j] < path[-1]:
                    continue
                if nums[j] in seen:
                    continue

                seen.add(nums[j])

                path.append(nums[j])
                backtrack(j+1,path)
                path.pop()

        backtrack(0,[])
        return res