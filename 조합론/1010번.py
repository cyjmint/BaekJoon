T = int(input())
for i in range(T):
    N,M = list(map(int,input().split()))
    n,m = 1,1
    for i in range(M-N+1, M+1):
        m*=i
    for i in range(1,N+1):
        n*=i
    print(m//n)
