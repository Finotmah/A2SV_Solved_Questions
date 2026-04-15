class Solution:
    def splitString(self, s: str) -> bool:
        
        def dfs(index, prev):
            if index == len(s):
                return True
            
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])
                
                if prev == -1 or prev - num == 1:
                    if dfs(i + 1, num):
                        return True
            
            return False
        
        for i in range(1, len(s)):
            first = int(s[:i])
            if dfs(i, first):
                return True
        
        return False