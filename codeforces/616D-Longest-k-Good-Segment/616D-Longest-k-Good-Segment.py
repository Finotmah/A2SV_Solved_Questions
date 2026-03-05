n, k = map(int,input().split())

a = list(map(int,input().split()))

num_dist = 0
seg_map = dict()

l = 0
r = 0
l_need = 0
r_need = 0
max_l = 0
while r < n:
    if seg_map.get(a[r], 0) == 0:
        num_dist += 1
    seg_map[a[r]] = seg_map.get(a[r], 0) + 1

    if num_dist > k:
        seg_map[a[l]] -= 1
        if seg_map[a[l]] == 0:
            num_dist -= 1
        l += 1
    
    if r - l + 1 > max_l:
        max_l = r - l + 1
        l_need = l + 1
        r_need = r + 1
    r += 1
print(l_need, r_need)