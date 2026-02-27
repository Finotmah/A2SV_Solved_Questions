n, m= map(int, input().split())

a = list(map(int,input().split()))

sums = 0
nums = 0
l = 0
for i in range(n):
    sums += a[i]
    while sums > m:
        sums -= a[l]
        l += 1
    nums += i - l + 1
    
print(nums)



