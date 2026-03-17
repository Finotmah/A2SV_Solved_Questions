class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cheapA = sorted(costs,key = lambda x:x[0]-x[1])
        
        min_c = 0
        n = len(costs)//2
        for i in range(n):
            min_c += cheapA[i][0]
        for i in range(n,2*n):
            min_c += cheapA[i][1]
        return min_c