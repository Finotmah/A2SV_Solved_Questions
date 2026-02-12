def beautiful():
    n = 5
    matrix = []
    for i in range(n):
        row = list(map(int,input().split()))
        matrix.append(row)
    min_ops = 0

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0:
                if j > 1:
                    min_ops += j - 2
                if j < 2:
                    min_ops += 2 - j
                if i > 1:
                    min_ops += i - 2
                if i < 2:
                    min_ops += 2 - i
    print(min_ops)

beautiful()


    
