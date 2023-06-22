T = int(input())
for i in range(T):
    H, W, N = list(map(int,input().split()))
    n = 0
    while H < N-H*n:
        n += 1
    print(100*(N-H*n)+n+1)