n, k = map(int, input().split())

a = list(map(int, input().split()))

frq = {}
l = 0
d = 0
res = 0

for r in range(n):
    if a[r] not in frq or frq[a[r]] == 0:
        d += 1
    frq[a[r]] = frq.get(a[r], 0) + 1

    while d > k:
        frq[a[l]] -= 1
        if frq[a[l]] == 0:
            d -= 1
        l += 1
    res += (r - l + 1)

print(res)