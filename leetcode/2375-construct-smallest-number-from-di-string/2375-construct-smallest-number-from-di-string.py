class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = []
        stack = []

        for i in range(len(pattern)+1):
            stack.append(str(i + 1))

            if len(pattern) == i or pattern[i] == 'I':
                while stack:
                    res.append(stack.pop())
        
        return ''.join(res)