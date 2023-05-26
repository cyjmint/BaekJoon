N = int(input())
data = list(map(int,input().split()))
x = [data[0], data[1]]
for i in range(N):
    if data[i] >= x[0]:
        x[0] = data[i]
    if data[i] <= x[1]:
        x[1] = data[i]
print(x[1], end = ' ')
print(x[0])

