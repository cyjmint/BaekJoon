A,B,C = list(map(int,input().split()))
D = int(input())

b,c = D//60, D%60
B += b; C += c
if C//60 >= 1:
    B += C//60; C -= 60*(C//60)
if B//60 >= 1:
    A += B//60; B -= 60*(B//60)
if A//24 >= 1:
    A -= 24*(A//24)
print(A, end=' '); print(B, end=' '); print(C)