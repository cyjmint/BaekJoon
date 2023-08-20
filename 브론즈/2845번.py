l,p = list(map(int,input().split()))
n = list(map(int,input().split()))
for i in range(len(n)):
    n[i] = n[i] - l*p
print(*n)