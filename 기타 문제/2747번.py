N = int(input())
n = []
for i in range(N+1):
    if i == 0:
        n.append(0)
    elif i == 1:
        n.append(1)
    else:
        n.append(n[i-2]+n[i-1])

print(n[-1])