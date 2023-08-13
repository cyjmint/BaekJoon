N = int(input())
n = set(map(int,input().split()))
M = int(input())
m = list(map(int,input().split()))

for i in range(M):
    if m[i] in n:
        m[i] = 1
    else:
        m[i] = 0
print(*m)