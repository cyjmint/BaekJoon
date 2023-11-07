n,m = map(int,input().split())
candy = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if i == 0 and j != 0:
            candy[i][j] = candy[i][j-1] + candy[i][j]
        if i != 0 and j == 0:
            candy[i][j] = candy[i-1][j] + candy[i][j]
        if i != 0 and j != 0:
            a = candy[i][j-1] + candy[i][j]
            b = candy[i-1][j] + candy[i][j]
            c = candy[i-1][j-1] + candy[i][j]
            candy[i][j] = max(a,b,c)

print(candy[n-1][m-1])