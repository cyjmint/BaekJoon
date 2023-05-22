#세 자리 수 곱셈
x = int(input())
y = int(input())

def digit(n):
    a = n//100
    b = n//10 - a*10
    c = n - (a*100 + b*10)
    return a, b, c

a, b, c = digit(y)

print(x*c)
print(x*b)
print(x*a)
print(x*y)
