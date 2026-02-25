t = int(input())

for _ in range(t):
    s = input()
    
    res = ""
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            if count % 2 == 1:
                res += s[i-1]
            count = 1
    
    # handle last block
    if count % 2 == 1:
        res += s[-1]
    
    print("".join(sorted(set(res))))
