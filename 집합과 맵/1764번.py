n,m = map(int,input().split())
a = set(input() for i in range(n))
b = set(input() for i in range(m))
c = a&b
print(len(c))
for v in sorted(list(c)):
    print(v)