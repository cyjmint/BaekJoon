A,B = list(map(int,input().split()))
A,B = max(A,B),min(A,B); r = A%B; AB = A*B
while r > 0:
    A,B = B,r
    r = A%B
print(AB//B)