t = int(input())
for _ in range(t):
    ans = 0
    n,m = map(int,input().split())
    for a in range(1,n-1):
        for b in range(a+1,n):
            x = (a**2+b**2+m)/(a*b)
            if x-int(x) == 0.0:
                ans += 1
    print(ans)