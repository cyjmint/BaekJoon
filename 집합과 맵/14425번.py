n,m = list(map(int,input().split()))
s = set(input() for i in range(n))
ss = list(input() for i in range(m))

num = 0
for i in range(m):
    if ss[i] in s:
        num += 1
print(num)