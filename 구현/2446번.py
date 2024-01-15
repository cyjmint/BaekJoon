n = int(input())
a = 2*n-1
for i in range(n-1):
    print(' '*i + '*'*(a-2*i))
print(' '*(n-1) + '*')
for i in range(n-1):
    print(' '*(n-(i+2)) + '*'*(3+2*i))

#다른 풀이
N = int(input())
a=0
for i in range(N-1):
    a = a + 1
    print(" "*i+"*"*(N*2-(i+a)))

a=N
for i in range(N, 0, -1):
    a=a-1
    print(" "*(i-1)+"*"*(N*2-(i+a)))