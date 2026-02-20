def optimal():
    n = int(input())
    points = list(map(int, input().split()))
    points.sort()
    median = points[(n - 1) // 2]

    print(median)

optimal()
