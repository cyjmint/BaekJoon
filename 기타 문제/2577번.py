A = int(input())
B = int(input())
C = int(input())

m = A*B*C
a = list(str(m))

for i in range(10):
    print(a.count(str(i)))
