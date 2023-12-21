m,seed,x1,x2 = map(int,input().split())
l=[]
for a in range(0,m+1):
    for c in range(0,m+1):
        if (a*seed+c)%m == x1 and (a*x1+c)%m == x2:
            l.append([a,c])
            break
print(*l[0])