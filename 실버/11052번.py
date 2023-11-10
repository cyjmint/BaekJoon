n = int(input())
p = list(map(int,input().split()))
cost = [0] * (n+1)
cost[1] = p[0]

for i in range(2,n+1):
    x = 0
    for j in range(1,i//2+1):
        x = max(cost[j]+cost[i-j],x)
    cost[i] = max(cost[1]*i,x,p[i-1])

print(cost[n])