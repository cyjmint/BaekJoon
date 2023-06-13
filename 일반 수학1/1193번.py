X = int(input())

n=1
a=1
while a<X:
    n += 1
    a = int(n*(n+1)/2)

b = a-X
if n%2 != 0:
    N = 1+b
    D = n-b
else:
    N = n-b
    D = 1+b

print('%d/%d'%(N,D))