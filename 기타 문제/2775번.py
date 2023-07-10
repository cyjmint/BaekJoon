t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    x = [i for i in range(1,n+1)] #0층
    a = 1
    while a <= k:
        a += 1
        xk = [] #k층
        for b in range(n):
            y = 0
            i = 0
            while i <= b:
                y += x[i]
                i += 1
            xk.append(y)
        x = xk
    print(x[-1])
