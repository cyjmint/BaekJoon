n,k = map(int,input().split())
a = [int(input()) for _ in range(n)]
num = 0

def coin(k):
    global num
    b = []
    if k == 0:
        return
    else:
        for v in a:
            x = k//v
            if x > 0:
                b.append(x)
            else:
                b.append(v)
        ind = b.index(min(b))
        k -= min(b)*a[ind]
        num += min(b)
        coin(k)

coin(k)
print(num)