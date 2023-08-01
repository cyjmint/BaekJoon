a,b = list(map(int,input().split()))
c,d = list(map(int,input().split()))

A = a*d + b*c
B = b*d
    
x,y = max(A,B),min(A,B);r = x%y
while r:
    x,y = y,r
    r = x%y
print(A//y, end = ' ')
print(B//y)