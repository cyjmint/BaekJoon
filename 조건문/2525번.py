H, M = list(map(int, input().split()))
C = int(input())

def oven(x,y,z):
    if x not in range(0,24) or y not in range(0,60) or z not in range(0,1001):
        pass
    else:
        m = (y+z)%60
        h = x + ((y+z)//60)
    if h >= 24:
        h -= 24
    return print(h, end = ' '), print(m)

oven(H,M,C)