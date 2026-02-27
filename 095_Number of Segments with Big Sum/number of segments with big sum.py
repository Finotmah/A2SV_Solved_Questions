n, m= map(int, input().split())

a = list(map(int,input().split()))

sums = 0
nums = 0
r = 0
for i in range(n):
    
    while sums < m and r < n:
        sums += a[r]
        r += 1
    
    if sums >= m:
        nums += n - r + 1
    sums -= a[i]
print(nums)



