n = int(input())
l = []
for _ in range(n):
    a = tuple(map(int,input().split()))
    l.append(a)

s_l = sorted(l, key=lambda x: [(x[1],x[0])] )

for v in s_l:
    print(*v)