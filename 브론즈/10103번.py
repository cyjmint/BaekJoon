n = int(input())
c = 100; s = 100
for _ in range(n):
    a,b = map(int,input().split())
    if a > b:
        s -= a
    if a < b:
        c -= b
    if a == b:
        pass

print(c)
print(s)