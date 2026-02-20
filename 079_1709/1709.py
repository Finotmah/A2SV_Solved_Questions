def numops():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        num_Ops = 0
        resutl = []
        
        for i in range(n):
            if a[i] > b[i]:
                a[i], b[i] = b[i],a[i]
                num_Ops += 1
                resutl.append((3,i+1))
        
        for i in range(n):
            for j in range(n-1-i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    num_Ops += 1
                    resutl.append((1,j+1))
                if b[j] > b[j+1]:
                    b[j], b[j+1] = b[j+1], b[j]
                    num_Ops += 1
                    resutl.append((2,j+1))

                
        
        print(num_Ops)
        for i in range(len(resutl)):
            print(resutl[i][0],resutl[i][1])
    

numops()
