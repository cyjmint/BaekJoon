T = int(input())
C = []
for i in range(T):
    C.append(int(input()))
    
Q = 25; D = 10; N = 5; P = 1

for i in range(len(C)):
    a = C[i] // Q
    b = (C[i]-Q*a) // D
    c = ((C[i]-Q*a)-D*b) // N
    d = (((C[i]-Q*a)-D*b)-N*c) // P
    print(a, end = ' ')
    print(b, end = ' ')
    print(c, end = ' ')
    print(d)
    