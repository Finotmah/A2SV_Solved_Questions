count = [0] * 101
        for num in nums:
            count[num] += 1
        
        # prefix sum: count of numbers smaller than i
        for i in range(1, 101):
            count[i] += count[i-1]
        
        res = []
        for num in nums:
            if num == 0:
                res.append(0)
            else:
                res.append(count[num-1])
        return res
