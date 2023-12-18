T = int(input())
for _ in range(T):
    n,m = map(int,input().split())
    u = m*2-n
    t = m-u
    print(u,t)