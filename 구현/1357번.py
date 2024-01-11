def Rev(n):
    l = list(str(n))
    x = 0
    for i in range(len(l)):
        x += int(l[i])*(10**i)
    return x

x,y = map(int,input().split())

print(Rev(Rev(x)+Rev(y)))