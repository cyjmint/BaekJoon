n = []
for i in range(7):
    N = int(input())
    if N%2 == 1:
        n.append(N)
if len(n) == 0:
    print(-1)
else:
    print(sum(n))
    print(sorted(n)[0])