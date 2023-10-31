p = []
def pm(n):
    if len(p) == n:
        print(*p)
        return
    else:
        for i in range(1,n+1):
            if i not in p:
                p.append(i)
                pm(n)
                p.pop()

pm(int(input()))