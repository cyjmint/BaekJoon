n,m,B = map(int,input().split())
l = [list(map(int,input().split())) for _ in range(n)]

num = []
for v in l:
    for number in v:
        num.append(number)

ans = []
for x in range(257):
    a = 0; b = 0
    for i in range(len(num)):
        if num[i] > x:
            a+=(num[i]-x)
        else:
            b+=(x-num[i])
    if a+B>=b:
        ans.append([2*a+b,x])

ans2 = sorted(ans,key = lambda x:(x[0],-x[1]))
print(*ans2[0])