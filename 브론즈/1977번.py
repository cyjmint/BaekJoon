M = int(input())
N = int(input())
n = []
for i in range(M,N+1):
    if i**.5-int(i**.5) == 0:
        n.append(i)
if len(n) == 0:
    print(-1)
else:
    print(sum(n))
    print(min(n))