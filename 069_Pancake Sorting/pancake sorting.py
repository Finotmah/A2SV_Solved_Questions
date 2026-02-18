class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for size in range(n, 1, -1):
            max_idx = arr.index(size)
            
            if max_idx == size - 1:
                continue 
            if max_idx != 0:
                res.append(max_idx + 1)
                arr[:max_idx+1] = reversed(arr[:max_idx+1])

            res.append(size)
            arr[:size] = reversed(arr[:size])
        
        return res
