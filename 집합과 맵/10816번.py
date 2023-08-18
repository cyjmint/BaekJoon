n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

dic = {}
for v in a:
    if v in dic:
        dic[v] += 1
    else:
        dic[v] = 1

for i in range(m):
    if b[i] in dic:
        b[i] = dic[b[i]]
    else:
        b[i] = 0
print(*b)