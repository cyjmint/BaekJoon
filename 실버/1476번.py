e,s,m = map(int,input().split())
x = 1; y = 1; z = 1; ans = 1

while True:
    if x == e and y == s and z == m:
        print(ans)
        break
    ans += 1
    if x >= 15:
        x = 1
    else:
        x += 1
    if y >= 28:
        y = 1
    else:
        y += 1
    if z >= 19:
        z = 1
    else:
        z += 1