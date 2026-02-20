def lastTime():

    t = int(input())
    for _ in range(t):

        n, k = map(int,input().split())

        casinos = []

        for i in range(n):
            l,r,real = map(int,input().split())

            casinos.append((l,r,real))
        
        casinos.sort()
        
        for i in range(n):
            if casinos[i][0] <= k <= casinos[i][1] and casinos[i][2] > k:
                k = casinos[i][2]
        
        print(k)
    
lastTime()
