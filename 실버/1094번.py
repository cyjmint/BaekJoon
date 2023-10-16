n = int(input())
x = [64]
while sum(x) > n:
    ind = x.index(min(x))
    a = min(x)//2; b = min(x)//2
    x.pop(ind)
    x.append(a)
    if sum(x) >= n:
        pass
    else:
        x.append(b)

print(len(x))