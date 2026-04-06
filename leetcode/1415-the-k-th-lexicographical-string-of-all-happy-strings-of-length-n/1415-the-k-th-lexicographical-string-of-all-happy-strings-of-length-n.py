class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        choice = ['a','b','c']
        def backtrack(path):
            if len(res) == k:
                return 
            if len(path) == n:
                res.append(''.join(path))
                return
            for char in choice:
                if path and path[-1] == char:
                    continue
                
                path.append(char)
                backtrack(path)
                path.pop()
            
        backtrack([])
        if k > len(res):
            return ""
        else:
            return res[k-1]

