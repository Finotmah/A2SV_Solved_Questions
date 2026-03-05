t = int(input())

for _ in range(t):
    n = int(input())

    a = input() 
    b = input()

    a += '0'
    b += '0'

    c0 = 0
    c1 = 0

    valid = True

    for i in range(n):
        if a[i] == '1':
            c1 += 1
        else:
            c0 += 1
        
        if (a[i] == b[i]) != (a[i+1] == b[i+1]):
            if c0 != c1:
                valid = False
                break
    if valid:
        print("YES")
    else:
        print("NO")