a = set()
b = set(i for i in range(1,10000))
def selfnum(n):
    if n < 10000:
        l = []
        num = n
        while num != 0:
            l.append(num%10)
            num = num//10
        ans = n+sum(l)
        if ans < 10000:
            a.add(ans)
        return selfnum(ans)
    else:
        return a
        
n = 1
while n < 10000:
    selfnum(n)
    n += 1

for v in a:
    b.remove(v)

for v in b:
    print(v)