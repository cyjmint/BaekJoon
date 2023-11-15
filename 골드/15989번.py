f = [[0]*4 for _ in range(10001)]
f[1][1] = 1
f[2][1] = 1
f[2][2] = 1
f[3][1] = 1
f[3][2] = 1
f[3][3] = 1

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(4,n+1):
        f[i][1] = f[i-1][1]
        f[i][2] = f[i-2][1] + f[i-2][2]
        f[i][3] = f[i-3][1] + f[i-3][2] + f[i-3][3]
    print(sum(f[n]))

#f[i][j] : 자연수 i를 j = [1,2,3]의 합으로 구성할 때, j로 끝나는 수식의 수