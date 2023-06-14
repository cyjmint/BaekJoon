M = int(input())
N = int(input())

PN = []
for i in range(M, N+1):
    f = []
    for j in range(1,i+1):
        if i%j == 0:
            f.append(j)
    if len(f) == 2:
        PN.append(i)

if len(PN) == 0:
    print(-1)
else:
    print(sum(PN))
    print(min(PN))


