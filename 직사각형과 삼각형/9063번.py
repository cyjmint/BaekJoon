N = int(input())
a = []
b = []
for i in range(N):
    data = list(map(int,input().split()))
    a.append(data[0])
    b.append(data[1])

x = max(a) - min(a)
y = max(b) - min(b)

print(x*y)