n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
ans = 0

while i < n and j < m:
    if a[i] < b[j]:
        i += 1
    elif a[i] > b[j]:
        j += 1
    else:
        # a[i] == b[j]
        val = a[i]        
        cnt_a = 0
        while i < n and a[i] == val:
            cnt_a += 1
            i += 1
                    
        cnt_b = 0
        while j < m and b[j] == val:
            cnt_b += 1
            j += 1
        
        ans += cnt_a * cnt_b

print(ans)
