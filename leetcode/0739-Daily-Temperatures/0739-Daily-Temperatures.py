class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack =[]
        num = 0
        res = [0]*len(temperatures)

        for i,temp in enumerate(temperatures):
            num = 0 
            while stack and temperatures[stack[-1]] < temp:
                num += 1
                idx = stack.pop()
                res[idx] = i - idx
            num = 0
            stack.append(i)
        
        return res