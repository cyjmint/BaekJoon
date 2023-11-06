n = int(input())
t = list(map(int,input().split()))
t = sorted(t,reverse=True)

for i in range(n):
    t[i] = t[i] - (n-(i+1))

print(n+max(t)+1)