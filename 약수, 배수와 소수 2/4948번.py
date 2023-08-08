while True:
    n = int(input())
    if n == 0:
        break
    else:
        l = [1]*(2*n+1)
        l[0],l[1] = 0,0
        for i in range(2,int((2*n)**.5)+1):
            if l[i] == 1:
                j = i
                while i*j <= 2*n:
                    l[i*j] = 0
                    j += 1
        x = 0
        for i in range(n+1,2*n+1):
            x += l[i]
        print(x)