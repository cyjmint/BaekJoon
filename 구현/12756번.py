a,b = map(int,input().split())
c,d = map(int,input().split())

while b > 0 and d > 0:
    b -= c
    d -= a

if b > 0:
    print('PLAYER A')
if d > 0:
    print('PLAYER B')
if b <= 0 and d <= 0:
    print('DRAW')