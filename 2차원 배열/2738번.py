N, M = list(map(int, input().split()))
A = []
B = []
for i in range(N):
    A.append(list(map(int,input().split())))
for j in range(N):
    B.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        S = A[i][j] + B[i][j]
print(S, end = ' ')
