n = int(input())
s = set()
num = 0
for i in range(n):
    a = input()
    if a == 'ENTER':
        num += len(s)
        s.clear()
    else:
        s.add(a)
print(num+len(s))