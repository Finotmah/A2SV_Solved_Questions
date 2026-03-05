t = int(input())

for _ in range(t):
    n = int(input())
    r = list(map(int,input().split()))

    m = int(input())
    b = list(map(int, input().split()))
    
    max_r = 0
    curr = 0
    for x in r:
        curr += x
        max_r = max(max_r, curr)

    max_b = 0
    curr = 0
    for x in b:
        curr += x
        max_b =  max( max_b, curr)
    
    print(max_r + max_b)