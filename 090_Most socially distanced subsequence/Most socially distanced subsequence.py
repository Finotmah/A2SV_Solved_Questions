t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))

    
    max_sum = float("-inf")
    points = [p[0]] # keep 1st element
    isup = True
    for right in range(1,n-1):
        if (p[right] - p[right-1]) * (p[right+1] - p[right]) < 0:
            points.append(p[right])
        
    points.append(p[-1])#add last element
    print(len(points))
    print(" ".join(map(str,points)))       
        
        
