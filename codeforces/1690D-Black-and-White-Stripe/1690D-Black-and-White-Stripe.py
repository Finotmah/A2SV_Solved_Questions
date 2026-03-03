t = int(input())
for _ in range(t):

    n, k = map(int, input().split())
    s = input().strip()
    w = s[:k].count('W')
    res = w
    
    for j in range(k,n):
        if s[j] == 'W':
            w +=1    
        if s[j - k] == 'W':
            w -= 1
        res = min(res, w)
    print(res)