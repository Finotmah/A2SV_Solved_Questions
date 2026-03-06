#horizontal starting mark
her_pr = [[0]*(c) for _ in range(r+1)]
for i in range(1,r+1):
    for j in range(1,c):
        if matrix[i-1][j-1] == '.' and matrix[i-1][j] == '.':
            her_pr[i][j] = 1
        else:
            her_pr[i][j] = 0

#horizontal prefixsum
for i in range(1,r+1):
    for j in range(1,c):
        her_pr[i][j] = her_pr[i][j] + her_pr[i-1][j] + her_pr[i][j-1] - her_pr[i-1][j-1]

#vertical starting mark
ver_pr = [[0]*(c+1) for _ in range(r)]
for i in range(1,r):
    for j in range(1,c+1):
        if matrix[i-1][j-1] == '.' and matrix[i][j-1] == '.':
            ver_pr[i][j] = 1
        else:
            ver_pr[i][j] = 0

#vertical prefixsum
for i in range(1,r):
    for j in range(1,c+1):
        ver_pr[i][j] = ver_pr[i][j] + ver_pr[i-1][j] + ver_pr[i][j-1] - ver_pr[i-1][j-1]


her_count = 0
ver_count = 0
for r1,c1,r2,c2 in querys:
    her_count = her_pr[r2][c2-1] - her_pr[r1-1][c2-1] - her_pr[r2][c1-1] + her_pr[r1-1][c1-1]
    ver_count = ver_pr[r2-1][c2] - ver_pr[r1-1][c2] - ver_pr[r2-1][c1-1] + ver_pr[r1-1][c1-1]
    print(her_count + ver_count)
    


#example matrix
# [['.', '.', '.', '.', '#', '.', '.', '#'], 
#  ['.', '#', '.', '.', '.', '.', '.', '.'], 
#  ['#', '#', '.', '#', '.', '.', '.', '.'], 
#  ['#', '#', '.', '.', '#', '.', '#', '#'], 
#  ['.', '.', '.', '.', '.', '.', '.', '.']]

#querys
# [[1, 1, 2, 3], 
#  [4, 1, 4, 1], 
#  [1, 2, 4, 5], 
#  [2, 5, 5, 8]]



#horizontal starting mark 
# [[0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 0, 0, 1, 0], 
#  [0, 0, 0, 1, 1, 1, 1, 1], 
#  [0, 0, 0, 0, 0, 1, 1, 1], 
#  [0, 0, 0, 1, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1]]

#horizonatal presum
# [[0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 2, 3, 3, 3, 4, 4], 
#  [0, 1, 2, 4, 5, 6, 8, 9], 
#  [0, 1, 2, 4, 5, 7, 10, 12], 
#  [0, 1, 2, 5, 6, 8, 11, 13], 
#  [0, 2, 4, 8, 10, 13, 17, 20]]



#vertical starting mark
# [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 0, 1, 1, 0, 1, 1, 0], 
#  [0, 0, 0, 1, 0, 1, 1, 1, 1], 
#  [0, 0, 0, 1, 0, 0, 1, 0, 0], 
#  [0, 0, 0, 1, 1, 0, 1, 0, 0]]

#vertical prefixsum
# [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 2, 3, 3, 4, 5, 5], 
#  [0, 1, 1, 3, 4, 5, 7, 9, 10], 
#  [0, 1, 1, 4, 5, 6, 9, 11, 12], 
#  [0, 1, 1, 5, 7, 8, 12, 14, 15]]