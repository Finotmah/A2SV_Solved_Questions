def array_split():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k >= n:
        print(0)
        return
    
    
    
    # Compute adjacent differences
    diffs = []
    for i in range(1, n):
        diffs.append(a[i] - a[i-1])
    
    # Sort differences descending
    diffs.sort(reverse=True)
    
    # Total range
    total = a[-1] - a[0]
    
    # Subtract k-1 largest gaps
    for i in range(k-1):
        total -= diffs[i]
    
    print(total)

array_split()
