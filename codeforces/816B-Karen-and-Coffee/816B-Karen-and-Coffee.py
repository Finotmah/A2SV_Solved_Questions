#prefix sum
for i in range(1,max_T + 1):
    c[i] += c[i - 1]
#mark good Temprature
for i in range(1,max_T + 1):
    c[i] = 1 if c[i] >= k else 0
for i in range(1,max_T + 1):
    c[i] += c[i-1]

for a, b in query:
    print(c[b] - c[a- 1])