A, B, V = list(map(int,input().split()))

n = int((V-A)/(A-B))
if (V-A)%(A-B) != 0:
    n = n+1
print(n+1)