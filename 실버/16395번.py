n,k = map(int,input().split())
num = [[0]*(i+1) for i in range(n)]
num[0] = [1]

for i in range(1,n):
    for j in range(i+1):
        if j == 0 or j == i:
            num[i][j] = 1
        else:
            num[i][j] = num[i-1][j-1] + num[i-1][j]

print(num[n-1][k-1])