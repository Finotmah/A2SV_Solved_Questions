def Dominant_char():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        if n == 1:
            print(-1)
        if "aa" in s:
            print(2)
        elif "aba" in s or "aca" in s:
            print(3)
        elif "abca" in s or "acba" in s:
            print(4)
        elif "abbacca" in s or "accabba"in s:
            print(7)
        else:
            print(-1)

Dominant_char()
