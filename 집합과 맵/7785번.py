n = int(input())
s = set()
for i in range(n):
    a,b = input().split()
    if a not in s:
        s.add(a)
    else:
        s.remove(a)

m = sorted(s, reverse = True)
for i in range(len(s)):
    print(m[i])