N = int(input())
data = list(map(int,input().split()))
v = int(input())
x = 0
for i in range(N):
    if data[i] == v:
        x += 1
print(x)