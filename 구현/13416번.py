t = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for _ in range(n):
        a,b,c = map(int,input().split())
        x = max(a,b,c)
        if x > 0:
            ans += x
        else:
            ans += 0
    print(ans)