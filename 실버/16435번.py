n,l = map(int,input().split())
h = list(map(int,input().split()))
h = sorted(h)

for i in range(n):
    if l < h[i]:
        pass
    else:
        l += 1

print(l)